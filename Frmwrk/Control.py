'''
Created on Dec 15, 2015
@author: v-leoche
'''
import Gather
import HTMLTestRunner
from Frmwrk import IContext

HTMLHelper = HTMLTestRunner.HTMLTestRunner
from Logger import Loger
import xml.sax
from Parse import ParseXMLTeamplate

#provide an interface to invoke if have an exception
def inform(varfails,varaborts,grbaborts):
    pass

'''
Config class is used to control the framework how to run
'''
class Config(object):
    def __init__(self,xml,log,html,opt,inform=None,**kdb):
        if xml is None:
            raise Exception('the path of xml is empty')
        if log is None:
            raise Exception('the path of log is empty')
        if html is None:
            raise Exception('the path of html is empty')

        #database
        con = None
        if kdb.get('start-up'):
            import Databases
            if kdb['engine'] == 'mysql':
                con = Databases.mysql('mysql')(**kdb['settings'])

        #xml
        varmap = Config.load_xml(xml)
        #log
        self.logger=Loger()
        self.logger.Open(log)

        #html
        self.fp_html = open(html, 'wb')
        #create the IContext,and Gather
        self.ctx = IContext(varmap=varmap,logger=self.logger,opt=opt,con=con)
        self.gather = Gather.Gather(HTMLTestRunner._TestResult(1), \
                                    htmlhelper=HTMLHelper(stream=self.fp_html, title='FTTReport', description='This is the report for FTT framework'))

    def __del__(self):
        self.gather.gather(self.ctx)
        #write the log
        self.logger.Colse()
        #write the html
        self.fp_html.close()
        #inform the expections
        if self.gather.IsExpection:
            inform(self.gather.lVarFail,self.gather.lVarAbort,self.gather.lGrpAbort)

    @staticmethod
    def load_xml(f):
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        Handler = ParseXMLTeamplate()
        parser.setContentHandler(Handler)
        parser.parse(f)
        return Handler.varMap

    #get the run model to determine code how to run
    def __call__(self, *args, **kwargs):
        if self.ctx.RunModel =='':
            '''
            None  the tool will run the all case in the varmap.Support this model in the future
            '''
            self.runServerByEmpty()
        elif self.ctx.RunModel=='v':
            '''
            v  the tool will run the specified case
            '''
            self.runServerByVid(self.ctx.RunModelVal)
        elif self.ctx.RunModel=='s':
            '''
            s  the tool will run the specified cases which set is the same
            '''
            self.runServerBySet(self.ctx.RunModelVal)

    def myRange(self,num):
        assert not num == type(int)
        if num ==0:
            return [0]
        else:
            return range(num)
        
    def run(self,cls):
        #new the object
        instance = cls()
        public_methods = [eval("instance."+method) for method in dir(instance) if callable(getattr(instance, method)) and not method.startswith('__')]
        flow_methods = dict([(method._SETUP_,method) for method in public_methods if hasattr(method,'_SETUP_')])
        while True:
            fun = yield
            yield self.gather(flow_methods[fun],self.ctx) if fun in flow_methods else True

    def next(self,generator,fun):
        if generator.send(fun):
            generator.send(None)
            return True
        else:
            generator.send(None)
            return False       
    
    def runServer(self,vid):
        #run the var
        self.ctx.Records = self.ctx.VarMap.getVarByVid(vid)
        for pid in self.myRange(self.ctx.Records.attributes['LenofRecm']):
            self.ctx.Records.setVarPid(pid)
            #TODO this will return a generator to detect the exception.
            cls = self.ctx.Records.reflect()
            gVar = self.run(cls)
            gVar.next()
            #Vars expected
            self.gather.varExpectedCount+=1
            #get var info
            self.gather.getVarInfo(self.ctx)
            #if GrpAbort
            if self.gather.IsGrpAbort:
                self.gather.varNotRunCount+=1
                self.gather.result(self.ctx)
            else:
                if self.next(gVar,'_FTT_Setup_') and self.next(gVar,'_FTT_Run_') and self.next(gVar,'_FTT_Verify_'):
                    self.next(gVar, '_FTT_Cleanup_')
                    #Var pass
                    self.gather.varPassCount+=1
                    self.gather.result(self.ctx,True)
                else:
                    self.next(gVar, '_FTT_Cleanup_')
                    self.gather.result(self.ctx)
            gVar.close()


    def runServerByVid(self,vid):
        #init the IContext
        self.ctx.Records = self.ctx.ParentContext
        self.ctx.Records.setVarPid(0)
        #switch class to instantiate
        cls = self.ctx.Records.reflect()
        #TODO this will return a generator to detect the exception.
        detect = self.run(cls)
        #start the generator
        detect.next()
        #run the GroupHelper.Setup method
        self.next(detect,'_FTT_Setup_')
        #run the specified case
        self.runServer(vid)
        self.ctx.Records = self.ctx.ParentContext
        #run the GroupHelper.Setup method
        self.next(detect,'_FTT_Cleanup_')
        #close the generator
        detect.close()

    def runServerBySet(self,varSet):
        #init the IContext
        self.ctx.Records = self.ctx.ParentContext
        self.ctx.Records.setVarPid(0)
        #switch class to instantiate
        cls = self.ctx.Records.reflect()
        #TODO this will return a generator to detect the exception.
        detect = self.run(cls)
        #start the generator
        detect.next()
        #run the GroupHelper.Setup method
        self.next(detect,'_FTT_Setup_')
        #run the var
        for vid in self.ctx.getVidBySet(varSet):
            self.runServer(vid)
        self.ctx.Records = self.ctx.ParentContext
        #run the GroupHelper.Setup method
        self.next(detect,'_FTT_Cleanup_')
        #close the generator
        detect.close()
    
    def runServerByEmpty(self):
        #init the IContext
        self.ctx.Records = self.ctx.ParentContext
        self.ctx.Records.setVarPid(0)
        #switch class to instantiate
        cls = self.ctx.Records.reflect()
        #TODO this will return a generator to detect the exception.
        detect = self.run(cls)
        #start the generator
        detect.next()
        #run the GroupHelper.Setup method
        self.next(detect,'_FTT_Setup_')
        #run all the var
        for vid in self.ctx.getAllVid():
            self.runServer(vid)
        self.ctx.Records = self.ctx.ParentContext
        #run the GroupHelper.Setup method
        self.next(detect,'_FTT_Cleanup_')
        #close the generator
        detect.close()