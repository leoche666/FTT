import threading
import os
import time
from Control import Config

class ThreadConfig(object):
    def __init__(self):
        self.threads=[]
        self.count =0
        self.sleep_time = 5

    def __call__(self,settings=None,xml=None,opt=None,log=None,html=None):
        self.max = settings.THREAD['LIMIT_THREAD']
        if settings.THREAD['ISTHREAD']:
            self.runXmlByThread(settings)
        else:
            #if have no arguments
            if xml == None or opt == None:
                Config(xml=settings.OPTIONS['xml'],log=settings.OPTIONS['log'],\
                       html=settings.OPTIONS['html'],opt=settings.OPTIONS['opt'],**settings.DATABASES)()
            else:
                Config(xml=xml,log=log,html=html,opt=opt,**settings.DATABASES)()


    def runXmlByThread(self,settings):
        xmlDir = os.listdir(settings.WORKDIRCTORY)
        for _dir in xmlDir:
            while True:
                if _dir.find('.xml')==-1:
                    break
                
                if self.count < self.max: 
                    fullPathXml = os.path.join(settings.WORKDIRCTORY,_dir)
                    fullPathLog =  os.path.join(settings.WORKDIRCTORY,_dir+'.log.txt')
                    fullPathLogXml = os.path.join(settings.WORKDIRCTORY,_dir+'.logxml.xml')
                    _thread = myThreadForConfig(self.count,_dir)
                    
                    _thread.setParams(fullPathXml,settings.OPTIONS['opt'],\
                                      fullPathLog, fullPathLogXml,settings.DATABASES)
                    _thread.start()
                    self.count = self.count + 1 
                    self.threads.append(_thread)
                    break
                else : 
                    time.sleep(self.sleep_time)               
                    for t in self.threads:
                        if t.isAlive():
                            continue
                        else:
                            self.threads.remove(t)
                            self.count = self.count - 1 
                                                  
        for t in self.threads:
            t.join()            
                

class myThreadForConfig(threading.Thread):
    def __init__(self,threadID="",name=""):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
       
    def setParams(self,xml,log,html,opt,kdb):
        self.xml = xml
        self.log = log
        self.html = html
        self.opt = opt
        self.kdb = kdb
    
    def run(self):
        Config(xml=self.xml,log=self.log,html=self.html,opt=self.opt,**self.kdb)()