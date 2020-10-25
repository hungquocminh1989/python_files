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
import sys, os, json, time, requests, numpy
from datetime import datetime
from urllib.parse import urlencode

#Import lib common
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOT_DIR + '/lib')
import common

username = 'MinhHung89'
password = ''
irepeat = 5
url_all = 'https://quizlet.com/537818148/edit' # Ôn tập tổng hợp
url_unit = 'https://quizlet.com/540393860/edit' # UNIT hiện tại
words = [
    'Generally=Nhìn chung, nói chung',
    'Throw a party=Lễ kỷ niệm',
    'Wedding party=Tiệc cưới',
    'Wedding=Lễ cưới',
    'National holiday=Ngày nghỉ lễ toàn quốc',
    'Pray for good luck=Cần vận may, cầu may mắn',
    'Loved ones=Những người thân yêu',
    'Feed at home=Tự nhiên như ở nhà',
]

# Generate words
data_import = ''
for v in words:
    w_en = v[0 : v.index('=')]
    w_vi = v[v.index('='):]
    word = numpy.repeat(w_en + '.', irepeat) 
    data_import += os.linesep.join(word) + w_vi + os.linesep*2

data_import = data_import.replace('=', "\t")

# Init web
browser = common.SeleniumInstance(session=False)
browser.set_timeout_waiting(1)

# Login
browser.action_redirect('https://quizlet.com/vi')
browser.action_input_click('//*[@id="SiteHeaderReactTarget"]/header/div[1]/div/div[2]/span[2]/div/div[3]/div/button[1]/span/span')
browser.action_input_text('//*[@id="username"]', username)
browser.action_input_text('//*[@id="password"]', password)
browser.action_input_click('/html/body/div[7]/div/div[2]/form/button/span/div/span')
browser.set_time_sleep_waiting(5)

# Import all
browser.action_redirect(url_all)
browser.action_input_click('//*[@id="SetPageTarget"]/div/div[1]/div[3]/div/button')
browser.action_input_text('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/div[2]/div[2]/div/label[3]/span[2]/span/label/div/input', '\\n\\n')
browser.action_input_text('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/textarea', data_import)
browser.set_time_sleep_waiting(5)
browser.action_input_click('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/div[1]/button/span/span')
browser.action_input_click('//*[@id="SetPageTarget"]/div/div[1]/div[1]/div/div/div/div[3]/button/span/span')

# Import unit
browser.action_redirect(url_unit)
browser.action_input_click('//*[@id="SetPageTarget"]/div/div[1]/div[3]/div/button')
browser.action_input_text('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/div[2]/div[2]/div/label[3]/span[2]/span/label/div/input', '\\n\\n')
browser.action_input_text('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/textarea', data_import)
browser.set_time_sleep_waiting(5)
browser.action_input_click('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/div[1]/button/span/span')
browser.action_input_click('//*[@id="SetPageTarget"]/div/div[1]/div[1]/div/div/div/div[3]/button/span/span')
