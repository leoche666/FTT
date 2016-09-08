'''
@author: v-leoche
@summary: FTT framework
'''
import traceback
from functools import wraps
##############################################################################
#----------------------------------FTT exceptions-----------------------------
##############################################################################
class FrameworkException(Exception):
    def __init__(self,msg):
        self.errorList = traceback.extract_stack(None, None)
        self.error = msg

    @property
    def ErrorList(self):
        return self.errorList

    @property
    def Error(self):
        return self.error

    def __str__(self, *args, **kwargs):
        return self.error

class VarAbort(FrameworkException):
    def __init__(self,msg):
        FrameworkException.__init__(self, msg)

class VarFail(FrameworkException):
    def __init__(self,msg):
        FrameworkException.__init__(self, msg)

class GroupAbort(FrameworkException):
    def __init__(self,msg):
        FrameworkException.__init__(self, msg)

class VarNotRun(FrameworkException):
    def __init__(self,msg):
        FrameworkException.__init__(self, msg)


class VarUnsupported(FrameworkException):
    def __init__(self,msg):
        FrameworkException.__init__(self, msg)


class VarmapException(FrameworkException):
    def __init__(self,msg):
        FrameworkException.__init__(self, msg)

class ThreadLimitException(Exception):
    def __init__(self,msg):
        self.error = msg

    def __str__(self, *args, **kwargs):
        return self.error
##############################################################################
#----------------------------------FTT exceptions-----------------------------
##############################################################################



##############################################################################
#----------------------------------FTT values mapping-------------------------
##############################################################################
'''
@summary: Variation context. Passed to user's variation class in run-time.
'''
class IContext(object):
    def __init__(self,varmap,logger,opt,con=None):
        self.varmap = varmap
        self.records = None
        self.logger = logger
        self.parentContext = varmap.grp
        self.runModel=opt.split(':')[0]
        self.runModelVal=opt.split(':')[-1]
        self.runModelDsc = {'v':'v  the tool will run the specified case',
                            's':'s  the tool will run the specified cases which set is the same',
                            '' :'   the tool will run the all case in the varmap'}
        self.con = con
        self.buffer=None


    @property
    def SqlCon(self):return self.con

    @property
    def Buffer(self):return self.buffer

    @Buffer.setter
    def Buffer(self,buf):self.buffer=buf

    @property
    def VarMap(self):return self.varmap

    @property
    def Records(self):return self.records

    @Records.setter
    def Records(self,value):
        self.records = value

    @property
    def ParentContext(self):return self.parentContext

    @property
    def RunModel(self):return self.runModel

    @property
    def RunModelVal(self):return self.runModelVal

    def Alw(self,msg,isPrtTime=True):
        self.logger.Alw(msg,isPrtTime)

    def Err(self,errorList,msg):
        self.logger.Err(errorList,msg)

    def GetErrMsgFromErrorList(self,errorList):
        return self.logger.GetErrMsgFromErrorList(errorList)

    def getVidBySet(self,varSet):
        return self.varmap.getVidBySet(varSet)

    def getAllVid(self):
        return self.varmap.getAllVid()
##############################################################################
#----------------------------------FTT values mapping-------------------------
##############################################################################


##############################################################################
#----------------------------------FTT decorator----------------------------------
#Group.Setup->Case.Setup->Case.Run->Case.Verify->Case.Cleanup->Group.Cleanup
##############################################################################
def Setup(func):
    setattr(func,'_SETUP_','_FTT_Setup_')
    @wraps(func)
    def inner_deco(*args, **kwargs):
        func(*args, **kwargs)
    return inner_deco

def Run(func):
    setattr(func,'_SETUP_','_FTT_Run_')
    @wraps(func)
    def inner_deco(*args, **kwargs):
        func(*args, **kwargs)
    return inner_deco

def Verify(func):
    setattr(func,'_SETUP_','_FTT_Verify_')
    @wraps(func)
    def inner_deco(*args, **kwargs):
        func(*args, **kwargs)
    return inner_deco

def Cleanup(func):
    setattr(func,'_SETUP_','_FTT_Cleanup_')
    @wraps(func)
    def inner_deco(*args, **kwargs):
        func(*args, **kwargs)
    return inner_deco

