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
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOT_DIR + '/lib')
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
        remote_url = 'http://10.211.55.3:4444/wd/hub'
        url = 'https://13.231.155.63/shop/gumma/yamadap/window/step1'
        #url = 'https://test.pattolixil-madohonpo.jp/shop/gumma/yamadap/window/step1'
        #url = 'https://stg.pattolixil-madohonpo.jp/shop/hokkaido/test3/window/step1'

        inplus_data_2 = {
            'step1' : {
                'product'   : '//*[@id="list-content"]/div[2]/ul/li[1]/div',
                'door'      : '//*[@id="list-content"]/div[4]/ul/li[1]/div',
                'next'      : '//*[@id="wrap-btn"]/div/form/button',
            },
            'step2' : {
                'color'     : '//*[@id="list-content"]/div/ul[2]/div[1]/div/li[1]/div',
                'next'      : '//*[@id="wrap-btn"]/div/form/button',
            },
            'step3' : {
                'width'     : '//*[@id="wrap-hw-chois"]/table/tbody/tr[1]/td[2]/select',
                'height'    : '//*[@id="wrap-hw-chois"]/table/tbody/tr[2]/td[2]/select',
                'next'      : '//*[@id="wrap-btn"]/form/button',
            },
            'result' : {
                'option_1'  : '//*[@id="list-content"]/section[2]/div[2]/div[2]/label/span[1]',
                'option_2'  : '//*[@id="list-content"]/section[2]/div[3]/div[2]/label/span[1]',
                'option_3'  : '//*[@id="list-content"]/section[2]/div[4]/div[2]/label/span[1]',
                'add_cart'  : '//*[@id="add_cart"]/button',
                'back_step3' : '//*[@id="breadcrumbs-one"]/li[3]/a',
                'price' : '//*[@id="price-total"]',
            }
        }
        
        inplus_data_price = [
                {
                    'door' : '2 枚建',
                    'width' : '1000',
                    'height' : '600',
                    'price_option_1' : '¥55,000',
                    'price_option_2' : '¥59,000',
                    'price_option_3' : '¥59,000',
                },
        ]
        
        self.browser = common.SeleniumInstance()
        
        #self.browser.set_time_sleep_waiting(1)
        self.browser.set_timeout_waiting(30)
        
        for item in inplus_data_price:
            self.browser.action_redirect(url)

            #step1
            self.browser.action_input_click(inplus_data_2['step1']['product'])
            self.browser.action_input_click(inplus_data_2['step1']['door'])
            self.browser.action_input_click(inplus_data_2['step1']['next'])

            #step2
            self.browser.action_input_click(inplus_data_2['step2']['color'])
            self.browser.action_input_click(inplus_data_2['step2']['next'])

            #step3
            self.browser.action_input_combobox(inplus_data_2['step3']['width'], item['width'])
            self.browser.action_input_combobox(inplus_data_2['step3']['height'], item['height'])
            self.browser.action_input_click(inplus_data_2['step3']['next'])

            #result
            self.browser.action_waiting(1)
            self.browser.action_input_click(inplus_data_2['result']['option_1'])
            self.browser.action_waiting(1)
            
            if self.browser.action_get_text(inplus_data_2['result']['price']) == item['price_option_1'] :
                self.browser.action_screenshot("{0}_({1}x{2})_option_1_OK.png".format(item['door'], item['width'], item['height']))
            else:
                self.browser.action_screenshot("{0}_({1}x{2})_option_1_NG.png".format(item['door'], item['width'], item['height']))

            
            self.browser.action_input_click(inplus_data_2['result']['option_2'])
            self.browser.action_waiting(1)

            if self.browser.action_get_text(inplus_data_2['result']['price']) == item['price_option_2'] :
                self.browser.action_screenshot("{0}_({1}x{2})_option_2_OK.png".format(item['door'], item['width'], item['height']))
            else:
                self.browser.action_screenshot("{0}_({1}x{2})_option_2_NG.png".format(item['door'], item['width'], item['height']))
            
            self.browser.action_input_click(inplus_data_2['result']['option_3'])
            self.browser.action_waiting(1)

            if self.browser.action_get_text(inplus_data_2['result']['price']) == item['price_option_3'] :
                self.browser.action_screenshot("{0}_({1}x{2})_option_3_OK.png".format(item['door'], item['width'], item['height']))
            else:
                self.browser.action_screenshot("{0}_({1}x{2})_option_3_NG.png".format(item['door'], item['width'], item['height']))

            #self.browser.action_input_click('//*[@id="wrap-btn"]/a[1]/button')
            #self.browser.close()
        
        
        

obj = autotest()
obj.test_mmen()
exit
