# -*- coding=utf-8 -*-
'''
Created on 2016年6月14日
@author: leoche
@summary:
'''
import sys
sys.path.append("../..")
from automation.FTT.Frmwrk.Frmwrk import VarAbort,Setup,Run,Verify,Cleanup
from automation.common.SeleniumExt import find_element_by_suffix
from automation.common.SeleniumExt import switch_to_window

class Flows(object):
    @Setup
    def Setup(self,ctx):
        self.buffer = {}
        ctx.Alw('Flows.Setup')
        self.driver = ctx.Buffer
        self.flows = [flow for flow in ctx.Records.findSniprefs()]

        if len(self.flows)!=4:
            raise VarAbort("Flows must have 4 setp")

        for key,val in self.flows[0]:
            ctx.Alw('key:%s val:%s in Flows.Setup'%(key,val))
            find_element_by_suffix(self.driver,key,val,self.buffer)
            switch_to_window(self.driver)

    @Run
    def Run(self,ctx):
        ctx.Alw('Flows.Run')
        for key,val in self.flows[1]:
            ctx.Alw('key:%s val:%s in Flows.Run'%(key,val))
            find_element_by_suffix(self.driver,key,val,self.buffer)
            switch_to_window(self.driver)



    @Verify
    def Verify(self,ctx):
        ctx.Alw('Flows.Verify')
        for key,val in self.flows[2]:
            ctx.Alw('key:%s val:%s in Flows.Verify'%(key,val))
            find_element_by_suffix(self.driver,key,val,self.buffer)
            switch_to_window(self.driver)


    @Cleanup
    def Cleanup(self,ctx):
        ctx.Alw('Flows.Cleanup')
        for key,val in self.flows[3]:
            ctx.Alw('key:%s val:%s in Flows.Cleanup'%(key,val))
            find_element_by_suffix(self.driver,key,val,self.buffer)
            switch_to_window(self.driver)

        #clean the buffer
        self.buffer.clear()



