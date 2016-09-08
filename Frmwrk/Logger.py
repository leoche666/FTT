'''
@author: v-leoche
@summary: The Loger can output the log of program
'''
import time

class Loger(object):
    def __init__(self):
        self.file=None
        self.fTime='%Y-%m-%d %X'
    
    '''
    @summary:  Log output with 'Always' priority/level.
    '''
    def Alw(self,msg,isPrtTime=True):
        if isPrtTime:
            tStr=time.strftime( self.fTime, time.localtime() ) + " : " + msg 
            print tStr
            self.file.write(tStr + '\n')
        else:
            print msg
            self.file.write(msg + '\n')

        self.file.flush()
    '''
    @summary:  Log output with 'Error' priority/level.
    '''
    def Err(self,errorList,msg):
        self.Alw(msg)
        """Print the list of tuples as returned by extract_tb() or
        extract_stack() as a formatted stack trace to the given file."""
        if errorList:
            errorList=errorList[0:-2]
            for filename, lineno, name, line in errorList:
                self.Alw('  File "%s", line %d, in %s' % (filename,lineno,name),False)
                if line:
                    self.Alw( '    %s' % line.strip(),False)


    def GetErrMsgFromErrorList(self,errorList):
        msg=""
        """Print the list of tuples as returned by extract_tb() or
        extract_stack() as a formatted stack trace to the given file."""
        if errorList:
            errorList=errorList[0:-2]
            for filename, lineno, name, line in errorList:
                msg = msg + '  File "%s", line %d, in %s' % (filename,lineno,name) + '\n'
                if line:
                    msg = msg + '    %s' % line.strip() + '\n'
        return msg


    def ExceptErr(self,msg):
        self.Alw(msg)
    
    '''
    @summary: Log output with 'Warning' priority/level.
    '''
    def Wrn(self,msg):
        pass
    
    '''
    @summary: Log output with 'Trace' priority/level.
    '''
    def Trc(self,msg):
        self.file.write(msg)
     
     
    '''
    @summary:  Returns logger object. 
    '''
    def GetLogger(self):
        return self
      
      
    def Open(self,f):
        self.file = file(f,'w')
        self.Alw('\n***LOG START***\n',False)

    def Colse(self):
        if self.file:
            self.Alw( '\n***LOG DONE***\n',False)
            self.file.close()