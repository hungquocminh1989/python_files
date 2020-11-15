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
import common

class FacebookInstance:
    def __init__(self, username, password, remote_url='', temp_user_data=False):
        self.remote_url = remote_url
        self.temp_user_data = temp_user_data
        self.username = username
        self.user_debug_const = f'[{username} DEBUG] - '
        self.password = password
        self.init_web_instance()
        self.init_web_url()

    def init_web_instance(self):
        self.browser = common.SeleniumInstance(remote_url=self.remote_url,session=f'Facebook_{self.username}', auto_detect_timeout=True, temp_user_data=self.temp_user_data)
        self.browser.enable_auto_screenshot()
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Object created')

    def init_web_url(self):
        self.profile_url = 'https://mobile.facebook.com/profile'
        self.home_url = 'https://mobile.facebook.com/home.php'
        self.login_url = 'https://mobile.facebook.com/login.php'

    def newfeeds(self):
        self.browser.action_redirect(self.home_url)
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Redirect to newfeeds')

    def profile(self):
        self.browser.action_redirect(self.profile_url)
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Redirect to profile')
        
        return None

    def login(self):
        is_login = self.check_login_status()
        
        if is_login == False:
            self.browser.action_redirect(self.login_url)
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Redirect to login : {self.login_url}')
            
            self.browser.action_input_text('//*[@id="m_login_email"]', self.username)
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Input username')
            
            self.browser.action_input_text('//*[@id="m_login_password"]', self.password)
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Input password')
            
            self.browser.action_input_click('//*[@id="u_0_4"]/button')
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Click login button')

            self.browser.action_waiting(2)

        return None

    def check_login_status(self):
        self.profile()
        exist = self.browser.action_check_exist_element('//*[@id="m_login_email"]')
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Check login status')
        if exist == False:
            return True

        return False

    def post_to_page(self, page_url, content, arr_images):
        self.browser.action_redirect(page_url)
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Redirect to : {page_url}')
        
        self.browser.action_input_click('//*[@id="action_bar"]/div[1]/a')
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Click button create new post')
        
        self.browser.action_input_text('/html/body/div[2]/div[1]/div/div[6]/div[5]/form/div[1]/textarea', content)
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Input post content')
        
        for image in arr_images:
            self.browser.action_autoit_upload_file('//*[@id="structured_composer_form"]/div[5]/div/div[1]/button[1]',image)
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Select and upload file image : {image}')
            
        self.browser.action_input_click('//*[@id="composer-main-view-id"]/div[1]/div/div[3]/div/button[1]')
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Click button post')

        return None

    def close(self):
        self.browser.close()
    
