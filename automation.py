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
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(CURRENT_DIR + '/lib')
import common

class FacebookInstance:
    def __init__(self, remote_url=''):
        self.remote_url = remote_url
        self.init_web_instance()
        self.init_web_url()

    def init_web_instance(self):
        self.browser = common.SeleniumInstance(remote_url=self.remote_url)
        self.browser.enable_auto_screenshot()
        self.browser.set_time_sleep_waiting(1)
        self.browser.set_timeout_waiting(30)

    def init_web_url(self):
        self.profile_url = 'https://mobile.facebook.com/profile'
        self.home_url = 'https://mobile.facebook.com/home.php'
        self.login_url = 'https://mobile.facebook.com/login.php'

    def home(self):
        self.browser.action_redirect(self.home_url)

    def profile(self):
        self.browser.action_redirect(self.profile_url)
        
        return None

    def login(self, username, password):
        self.browser.action_redirect(self.login_url)
        self.browser.action_input_text('//*[@id="m_login_email"]', username)
        self.browser.action_input_text('//*[@id="m_login_password"]', password)
        self.browser.action_input_click('//*[@id="u_0_4"]/button')

        #self.profile()

        return None

    def check_login_status(self):

        return None
