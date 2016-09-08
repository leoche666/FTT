# -*- coding=utf-8 -*-
'''
Created on 2016年8月10日
@author: leoche
@summary: 野兽派官网接口自动化监测
'''
import sys
sys.path.append("../..")
from automation.FTT.Frmwrk.Frmwrk import Setup,Cleanup,GroupAbort

class Group(object):
    def __init__(self):
        pass

    @Setup
    def GroupStart(self,ctx):
        ctx.Alw('Initiate the environment in Group.Setup')


    @Cleanup
    def GroupEnd(self,ctx):
        ctx.Alw('Clean the environment in Group.Cleanup')