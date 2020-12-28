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
    def __init__(self, username, password, dynamic_user_data=False):
        self.config = common.Config().load_config()
        self.dynamic_user_data = dynamic_user_data
        self.username = username
        self.user_debug_const = f'[{username} DEBUG] - '
        self.password = password
        self.init_web_instance()
        self.init_web_url()
        self.cloudinary = common.Cloudinary(cloud_name='minty', api_key='826583412123261', api_secret='Sa3_O7wQUNvwnQELh8U313D5IvQ')

    def init_web_instance(self):
        self.browser = common.SeleniumInstance(session=f'Facebook_{self.username}', auto_detect_timeout=True, dynamic_user_data=self.dynamic_user_data)
        #self.browser.enable_auto_screenshot()
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Object created')

    def init_web_url(self):
        self.profile_url = self.config['FACEBOOK_URL']['PROFILE_URL']
        self.home_url = self.config['FACEBOOK_URL']['HOME_URL']
        self.login_url = self.config['FACEBOOK_URL']['LOGIN_URL']

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
            
            self.browser.action_input_text(self.config['FACEBOOK_XPATH']['EMAIL'], self.username)
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Input username')
            
            self.browser.action_input_text(self.config['FACEBOOK_XPATH']['PASSWORD'], self.password)
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Input password')
            
            self.browser.action_input_click(self.config['FACEBOOK_XPATH']['BUTTON_LOGIN'])
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Click login button')

            self.browser.action_waiting(2)

        return None

    def check_login_status(self):
        self.profile()
        exist = self.browser.action_check_exist_element(self.config['FACEBOOK_XPATH']['EMAIL'])
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Check login status')
        if exist == False:
            return True

        return False

    def post_to_page(self, page_url, content, arr_images):
        self.browser.action_redirect(page_url)
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Redirect to : {page_url}')
        
        self.browser.action_input_click(self.config['FACEBOOK_XPATH']['BUTTON_CREATE_POST'])
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Click button create new post')
        
        self.browser.action_input_text(self.config['FACEBOOK_XPATH']['TEXTBOX_CONTENT_POST'], content)
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Input post content')
        
        for image in arr_images:
            self.browser.action_autoit_upload_file(self.config['FACEBOOK_XPATH']['BUTTON_UPLOAD_IMAGE_POST'],self.browser.action_download_file(image))
            self.browser.dblogs.debug_log(f'{self.user_debug_const}Select and upload file image : {image}')
            
        self.browser.action_input_click(self.config['FACEBOOK_XPATH']['BUTTON_PUBLISH_POST'])
        self.browser.dblogs.debug_log(f'{self.user_debug_const}Click button post')

        return None

    def close(self):
        self.browser.close()
    
