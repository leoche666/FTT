# -*- coding=utf-8 -*-
import cookielib
import re
import urllib,urllib2
import sys
sys.path.append("../..")
from automation.FTT.Frmwrk.Frmwrk import VarAbort

def convertStrToDict(content):
    r_false = re.compile('false')
    r_true = re.compile('true')
    r_null = re.compile('null')
    content = r_false.sub('False',content)
    content = r_true.sub('True',content)
    content = r_null.sub('None',content)
    return eval(content)

def login(ctx,user,password,login_url):
    # Enable cookie support for urllib2 
    cookiejar = cookielib.CookieJar()
    urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    data = dict([("loginName",user),("password",password)])
    req = urlOpener.open(login_url, urllib.urlencode(data))
    log_result = convertStrToDict(req.read())

    '''
    Verify the log in successfully
    '''
    if log_result['success']:
        ctx.Alw("野兽派官网登录成功")
        #store the cookies
        cookies = req.info()['Set-Cookie']
    else:
        raise VarAbort(log_result['message'])

    return urlOpener,cookies