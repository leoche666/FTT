from time import sleep

import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append("../..")
from automation.FTT.Frmwrk.Frmwrk import VarAbort,VarFail

time_out=10

def switch_to_window(driver):
    sleep(1)
    driver.switch_to_window(driver.window_handles[-1])

def find_locator_by_option(option,value):
    if option == 'id':
        return (By.ID,value)
    elif option == 'xpath':
        return (By.XPATH,value)
    elif option == 'linktext':
        return (By.LINK_TEXT,value)
    elif option == 'css':
        return (By.CSS_SELECTOR,value)
    else:
        return (None,None)

def find_element_by_syn(driver,value_list):
    element = None
    for key,val in map(lambda str:tuple(str.split('=')),value_list):
        locator = find_locator_by_option(key,val)
        if element is None:
            ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
            element = EC.visibility_of_element_located(locator)(driver)
        else:
            element = element.find_element(*locator)
    return element


def find_element_by_suffix(driver,key,val,buffer=None):
    try:
        function = key.split('_')[0]
        option = key.split('_')[-1]
        isSyn = lambda option:True if option == 'syn' else False

        if function == 'url':
            driver.get(val)
            #old_page = driver.find_element_by_tag_name('html')
            #ui.WebDriverWait(driver, time_out).until(EC.staleness_of(old_page))
        elif function == 'click':
            if isSyn(option):
                element = find_element_by_syn(driver,val.split(','))
            else:
                locator = find_locator_by_option(option,val)
                ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
                element = EC.element_to_be_clickable(locator)(driver)
            element.click()
        elif function == 'sendkeys':
            if isSyn(option):
                element = find_element_by_syn(driver,val.split(',')[1:])
            else:
                locator = find_locator_by_option(option,val.split(',')[-1])
                ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
                element = EC.visibility_of_element_located(locator)(driver)
            element.send_keys(val.split(',')[0])
        elif function == 'none':
            if isSyn(option):
                find_element_by_syn(driver,val.split(','))
            else:
                locator = find_locator_by_option(option,val)
                ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
                EC.visibility_of_element_located(locator)(driver)
        elif function == 'get':
            if isSyn(option):
                element = find_element_by_syn(driver,val.split(','))
            else:
                locator = find_locator_by_option(option,val)
                ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
                element = EC.visibility_of_element_located(locator)(driver)
            buffer[key] = element.text
        elif function == 'getAttribute':
            if isSyn(option):
                element = find_element_by_syn(driver,val.split(','))
            else:
                locator = find_locator_by_option(option,val.split(',')[-1])
                ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
                element = EC.visibility_of_element_located(locator)(driver)
            buffer[key] = element.get_attribute(val.split(',')[0])
        elif function == 'getByfilter':
            if isSyn(option):
                element = find_element_by_syn(driver,val.split(','))
            else:
                locator = find_locator_by_option(option,val.split(',')[-1])
                ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
                element = EC.visibility_of_element_located(locator)(driver)
            myfilter = eval(val.split(',')[0])
            buffer[key] = myfilter(element.text)
        elif function == 'verify':
            if isSyn(option):
                element = find_element_by_syn(driver,val.split(','))
            else:
                verify_context = ""
                if val.split(',')[0][0] == '$':
                    verify_context = buffer[val.split(',')[0][1:]]
                else:
                    verify_context = val.split(',')[0]
                locator = find_locator_by_option(option,val.split(',')[-1])
                ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
                element = EC.visibility_of_element_located(locator)(driver)
            if verify_context not in element.text:
                raise VarFail("Verify failed:" + verify_context)
        elif function == 'touch':
            if isSyn(option):
                element = find_element_by_syn(driver,val.split(','))
            else:
                touch = webdriver.TouchActions(driver)
                locator = find_locator_by_option(option,val)
                ui.WebDriverWait(driver, time_out).until(EC.visibility_of_element_located(locator))
                element = EC.visibility_of_element_located(locator)(driver)
            touch.tap(element).perform()
        elif function == 'script':
            js = val.split(',')[0]
            if len(val.split(','))==1:
                driver.execute_script(js)
            else:
                parms = map(lambda pa:buffer[pa[1:]] if pa[0]=='$' else pa,val.split(',')[1:])
                driver.execute_script(js,parms)
        elif function == 'post':
            account,password,method = val.split(',')[:3]
            parms = map(lambda pa:buffer[pa[1:]] if pa[0]=='$' else pa,val.split(',')[3:])
            eval("WebsiteHelper()()." + method)(*parms)
        elif function == 'alert':
            alert = driver.switch_to.alert
            eval("alert."+val+"()")
    except Exception,ex:
        raise VarAbort(ex.__str__())
