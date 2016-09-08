'''
Created on Jan 4, 2016

@author: v-leoche
'''
from Frmwrk import VarAbort,VarFail
import datetime

result={'abort':'ABORT','grp_abort':'GRP_ABORT','grp_fail':'GRP_FAIL','grp_pass':'GRP_PASS','step_fail':'STEP_FAIL',\
        'var_pass':'VAR_PASS','var_abort':'VAR_ABORT','var_fail':'VAR_FAIL','var_manual':'VAR_MANUAL','var_notrun':'VAR_NOTRUN',
        'var_unsupported':'VAR_UNSUPPORTED'}

class Gather(object):
    def __init__(self,unitTestResult,htmlhelper):
        self.startTime = datetime.datetime.now()
        self.HtmlResult = []
        self.lVarFail=[]
        self.lVarAbort=[]
        self.lGrpAbort=[]
        
        self.isGrpAbort=False
        self.varExpectedCount=0
        self.varPassCount=0
        self.varAbortCount=0
        self.varFailCount=0
        self.grpFailCount=0
        self.grpAbortCount=0
        self.varNotRunCount=0
        
        self.varResult=""
        self.unitTestResult = unitTestResult
        self.htmlhelper = htmlhelper

    '''
    @summary: this function will detect the flow of GroupHelper or your model.
    Note that each type of exception is treated slightly differently.
    GrpAbort will stop execution of all other variations in the parent group while VarAbort and VarFail only stop the current variation
    '''
    def __call__(self, *args, **kwargs):
        fun,ctx = args
        try:
            fun(ctx)
        except Exception,ex:
            if ctx.Records.userObject is ctx.ParentContext.userObject:
                self.detectForGrp(fun,ctx,ex)
            else:
                self.detectForVar(fun,ctx,ex)
            return False

        #add the result to html
        if ctx.Records.userObject is ctx.ParentContext.userObject:
            self.HtmlResult.append((None,(0, fun, '', '')))
        else:
            self.HtmlResult.append((ctx.Records.attributes.get('dsc'),(0, fun, '', '')))
        return True

    @property
    def IsGrpAbort(self):
        return self.isGrpAbort

    def detectForGrp(self,fun,ctx,ex):
        import traceback
        ctx.Alw(traceback.format_exc())
        #add the result to html
        self.lGrpAbort.append(traceback.format_exc())
        self.HtmlResult.append((ctx.Records.attributes.get('dsc'),(2, fun, ex.__str__(), traceback.format_exc())))
        self.varResult = result['var_notrun']
        self.isGrpAbort=True

    def detectForVar(self,fun,ctx,ex):
        if ex.__class__.__name__ is VarFail.__name__:
            ctx.Err(ex.ErrorList,ex.__str__())
            self.varResult = result['var_fail']
            self.varFailCount = self.varFailCount + 1
            #add the result to html
            errorList = ctx.GetErrMsgFromErrorList(ex.ErrorList)
            self.lVarFail.append(errorList)
            self.HtmlResult.append((ctx.Records.attributes.get('dsc'),(1, fun, ex.__str__(), errorList)))
        elif ex.__class__.__name__ is VarAbort.__name__:
            ctx.Err(ex.ErrorList,ex.__str__())
            self.varResult = result['var_abort']
            self.varAbortCount = self.varAbortCount + 1
            #add the result to html
            errorList = ctx.GetErrMsgFromErrorList(ex.ErrorList)
            self.lVarAbort.append(errorList)
            self.HtmlResult.append((ctx.Records.attributes.get('dsc'),(2, fun, ex.__str__(), errorList)))
        else :
            import traceback
            ctx.Alw(traceback.format_exc())  
            self.varResult = result['var_abort']
            self.varAbortCount = self.varAbortCount + 1
            #add the result to html
            self.lVarAbort.append(traceback.format_exc())
            self.HtmlResult.append((ctx.Records.attributes.get('dsc'),(2, fun, ex.__str__(), traceback.format_exc())))

    def getVarInfo(self,ctx):
        ctx.Alw('vid:%s lvl:%s  cid:%s  dsc:%s' % \
            (ctx.Records.attributes.get('vid'),ctx.Records.attributes.get('lvl'),ctx.Records.attributes.get('cid'),ctx.Records.attributes.get('dsc')),False)
     
  
    def result(self,ctx,isPass=False):
        if isPass:
            ctx.Alw(ctx.Records.attributes.get('dsc') + ' : %s\n' % result['var_pass'] ,False)
        else:
            ctx.Alw(ctx.Records.attributes.get('dsc') + ' : %s\n' % self.varResult,False)

    def gather(self,ctx):
        #generate the log
        self.stopTime = datetime.datetime.now()
        ctx.Alw( 'Vars expected    :[%d]'  % self.varExpectedCount   ,False)
        ctx.Alw( 'Vars passed      :[%d]'  % self.varPassCount       ,False)
        ctx.Alw( 'Vars aborted     :[%d]'  % self.varAbortCount      ,False)  
        ctx.Alw( 'Vars failed      :[%d]'  % self.varFailCount       ,False)
        ctx.Alw( 'Grps failed      :[0]'                             ,False)
        ctx.Alw( 'Grps aborted     :[0]'                             ,False)
        ctx.Alw( 'Vars unsupported :[0]'                             ,False)
        ctx.Alw( 'Vars Not Run     :[%d]'  %  self.varNotRunCount    ,False)

        #generate the html
        self.unitTestResult.success_count = self.varPassCount
        self.unitTestResult.failure_count = self.varFailCount
        self.unitTestResult.error_count   = self.varAbortCount + self.varNotRunCount
        self.unitTestResult.result = self.HtmlResult
        self.htmlhelper.startTime = self.startTime
        self.htmlhelper.stopTime = self.stopTime
        self.htmlhelper.generateReport(None,self.unitTestResult)

    @property
    def IsExpection(self):
        return self.varExpectedCount != self.varPassCount