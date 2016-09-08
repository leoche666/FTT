# -*- coding=utf-8 -*-
'''
Created on 2016年8月10日
@author: leoche
@summary: 验证在登陆官网之后能查询购物车
'''
import Login
import sys
sys.path.append("../..")
from automation.FTT.Frmwrk.Frmwrk import Setup,Run,Verify,Cleanup,VarFail,VarAbort

class Cart(object):
    def __init__(self):
        pass

    @Setup
    def CartSetup(self,ctx):
        self.user = ctx.Records.getValue('user')
        self.password = ctx.Records.getValue('password')
        self.login_url = ctx.Records.getValue('login_url')
        self.cart_url = ctx.Records.getValue('cart_url')

    @Run
    def CartRun(self,ctx):
        self.urlOpener,self.cookies = Login.login(ctx,self.user,self.password,self.login_url)

        req = self.urlOpener.open(self.cart_url)
        self.cart_result = Login.convertStrToDict(req.read())

    @Verify
    def CartVerify(self,ctx):
        if self.cart_result['code'] >= 200 and self.cart_result['code'] <= 300:
            if self.cart_result['message'] == '成功':
                pass
            else:
                raise VarFail("return message is %s" % self.cart_result['message'])
        else:
            raise VarAbort("query the cart unsuccessfully.ErrorCode : %d" % self.cart_result['code'])

    @Cleanup
    def CartCleanup(self,ctx):
        pass
