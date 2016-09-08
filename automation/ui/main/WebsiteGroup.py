# -*- coding=utf-8 -*-
'''
Created on 2016年6月14日
@author: leoche
@summary: Thebeastshop网站和M站购物流程自动化
'''
import os
import sys
sys.path.append("../..")
from selenium import webdriver
from automation.FTT.Frmwrk.Frmwrk import GroupAbort,Setup,Run,Verify,Cleanup


class Group(object):
    def __init__(self):pass

    @Setup
    def Setup(self,ctx):
        ctx.Alw('Initiate the environment in Group.Setup')
        #raise GroupAbort("test GroupAbort")

        #get the path of chromedriver
        chromedriver = ctx.Records.getValue('chromedriver')
        if not chromedriver:
            raise GroupAbort("chromedriver路径不能为空")

        #get the website
        website = ctx.Records.getValue('website')
        if not website:
            raise GroupAbort("网址不能为空")

        #open the chrome
        chromedriver_path=os.path.abspath(chromedriver)
        self.driver = webdriver.Chrome(chromedriver_path)
        self.driver.get(website)

        #put something into my buffer,it can use during next flow
        ctx.Buffer=self.driver

    @Cleanup
    def Cleanup(self,ctx):
        ctx.Alw('Clean the environment in Group.Cleanup')
        ctx.Buffer.quit()