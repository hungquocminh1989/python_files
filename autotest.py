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
import sys, os, json, time, requests
from datetime import datetime
from urllib.parse import urlencode

#Import lib common
sys.path.append('lib')
import common


# Download the helper library from https://www.twilio.com/docs/python/install
#from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
'''
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+',
         to='+'
     )

print(message.sid)
exit
'''

class autotest:
    def __init__(self):
        self.shared = common.Shared()
        self.vultr = common.VultrInstance('QTHEFETRVWWU7MTCVLSBHZL5E2ME6R4FX3NQ')
        #self.remoting = common.Remoting("149.28.147.3", 15, "root", "")
        
    def run(self):        
        
        #r = self.vultr.create_server()
        #info = self.vultr.get_server_info('27676263')
        #print(info)
        #proxy = common.ProxyX(hostname=info['main_ip'], password=info["default_password"], port='15')
        #proxy.start()
        
        #self.vultr.get_startupscript_list()
        self.browser = common.SeleniumInstance()
        self.browser.action_redirect('https://api.ipify.org/')
        self.browser.action_redirect('https://m.facebook.com/reg')
        
        #self.browser._save_cookies()
        self.browser.action_input_text('//*[@id="firstname_input"]', 'Hoang')#Firstname
        self.browser.action_input_text('//*[@id="lastname_input"]', 'Dung')#Lastname
        #self.browser.action_implicitly_wait(10)
        self.browser.action_input_click('//*[@id="mobile-reg-form"]/*/div[2]/button[1]')#Next
        
        self.browser.action_input_combobox('//*[@id="month"]', value='3')#month
        self.browser.action_input_combobox('//*[@id="day"]', value='15')#day
        self.browser.action_input_combobox('//*[@id="year"]', value='1997')#year
        self.browser.action_input_click('//*[@id="mobile-reg-form"]/*/div[2]/button[1]')#Next

        #self.browser.set_implicitly_wait(10)
        self.browser.action_input_click('//*[@id="mobile-reg-form"]/div[10]/div/a[1]')#Link to mail

        self.browser.action_input_text('//*[@id="contactpoint_step_input"]', 'nguyenhongduy1987@gmail.com')#Mail
        #self.browser.set_implicitly_wait(10)
        self.browser.action_input_click('//*[@id="mobile-reg-form"]/*/div[2]/button[1]')#Next

        self.browser.action_input_click('//*[@id="Nữ"]')#Female
        #self.browser.set_implicitly_wait(10)
        self.browser.action_input_click('//*[@id="mobile-reg-form"]/*/div[2]/button[1]')#Next

        self.browser.action_input_text('//*[@id="password_step_input"]', 'grdsfỵt12g5gj')#Password
        #self.browser.set_implicitly_wait(10)
        self.browser.action_input_click('//*[@id="mobile-reg-form"]/*/div[2]/button[4]')#Next

        #self.vultr.destroy_server(r['SUBID'])

    def run1(self):
        info = self.vultr.get_server_info('27676263')
        #print(info)
        proxy = common.ProxyX(hostname=info['main_ip'], password=info["default_password"], port='15', setting_proxy=True)
        proxy.start()

    def test_mmen(self):
        url = 'https://13.231.155.63/shop/yamagata/testshop1/window/step1'
        self.browser = common.SeleniumInstance()
        
        #self.browser.set_time_sleep_waiting(1)
        self.browser.set_timeout_waiting(30)
        
        for i in range(1):
            self.browser.action_redirect(url)
            #self.browser.action_input_click('//*[@id="list-content"]/div[2]/ul/li[1]/div')
            self.browser.action_input_click('//*[@id="list-content"]/div[4]/ul/li[1]/div')
            self.browser.action_input_click('//*[@id="wrap-btn"]/div/form/button')
            self.browser.action_input_click('//*[@id="list-content"]/div/ul[1]/li[3]/div')
            self.browser.action_input_click('//*[@id="wrap-btn"]/div/form/button')
            self.browser.action_input_combobox('//*[@id="wrap-hw-chois"]/table/tbody/tr[1]/td[2]/select', '1000')
            self.browser.action_input_combobox('//*[@id="wrap-hw-chois"]/table/tbody/tr[2]/td[2]/select', '600')
            self.browser.action_input_click('//*[@id="wrap-btn"]/form/button')
            self.browser.action_input_click('//*[@id="add_cart"]/button')
            #self.browser.action_input_click('//*[@id="wrap-btn"]/a[1]/button')
        
        
        

obj = autotest()
obj.run()
exit
