#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""
#-----------------------------------------------------------------------------
# Name:        
#
# Purpose:
#
# Version:     1.1
#
# Author:
#
# Created:     06/02/2020
# Updated:     06/02/2020
#
# Copyright:   -
#
#-----------------------------------------------------------------------------
#Check and update outdated packages
#pip install pipupgrade
#pipupgrade --check
#pipupgrade --latest --yes
#
#Export/Import environments
#pip freeze -l > requirements.txt
#pip install -r /path/to/requirements.txt
#-----------------------------------------------------------------------------
"""

#Import packages
import sys, os, json, time
from datetime import datetime
from urllib.parse import urlencode

#Import lib common
sys.path.append('lib')
import common

class autotest:
    def __init__(self):
        self.shared = common.Shared()
        self.vultr = common.VultrInstance('')
        #self.remoting = common.Remoting("149.28.147.3", 15, "root", "")
        
    def run(self):
        #r = self.vultr.create_server()
        info = self.vultr.get_server_info('27676263')
        #print(info)
        proxy = common.ProxyX(hostname=info['main_ip'], password=info["default_password"], port='15')
        proxy.start()
        #self.vultr.destroy_server('38784580')
        #self.vultr.get_startupscript_list()
        self.browser = common.SeleniumInstance()
        self.browser.set_redirect('https://api.ipify.org/')
        self.browser.set_redirect('https://m.facebook.com/reg', 5)
        #self.browser._save_cookies()
        self.browser.set_input_text('//*[@id="firstname_input"]', 'Nguyen')#Firstname
        el = self.browser.set_input_text('//*[@id="lastname_input"]', 'Dung')#Lastname
        #self.browser.enter(el)#Next
        self.browser.set_input_click('//*[@id="mobile-reg-form"]/div[8]/div[2]/button[1]')#Next
        
        self.browser.set_input_combobox('//*[@id="month"]', value='3')#month
        self.browser.set_input_combobox('//*[@id="day"]', value='15')#day
        self.browser.set_input_combobox('//*[@id="year"]', value='1997')#year
        self.browser.set_input_click('//*[@id="mobile-reg-form"]/div[8]/div[2]/button[1]')#Next
        
        self.browser.set_input_click('//*[@id="mobile-reg-form"]/div[10]/div/a[1]')#Link to mail

        self.browser.set_input_text('//*[@id="contactpoint_step_input"]', 'oukgjg@gmail.com')#Mail
        self.browser.set_input_click('//*[@id="mobile-reg-form"]/div[8]/div[2]/button[1]')#Next

        self.browser.set_input_click('//*[@id="Female"]')#Female
        self.browser.set_input_click('//*[@id="mobile-reg-form"]/div[8]/div[2]/button[1]')#Next

        self.browser.set_input_text('//*[@id="password_step_input"]"]', 'aocufkeh123')#Password
        self.browser.set_input_click('//*[@id="mobile-reg-form"]/div[8]/div[2]/button[1]')#Next
        #time.sleep(5000)
        #self.browser.set_input_click('/html/body/div/div/main/div[48]/form/div/div[1]/select/option[3222222]')
        

obj = autotest()
obj.run()
exit
