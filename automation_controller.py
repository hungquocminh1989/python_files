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
import os, sys, _thread, time

#Import lib common
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOT_DIR + '/lib')
import common, automation
import cloudinary.uploader

def f1():
    f1 = automation.FacebookInstance(username='@gmail.com',password='')
    f1.login()
    f1.post_to_page(page_url='https://mobile.facebook.com/1322105514589118', content='post1', arr_images=['https://res.cloudinary.com/minty/image/upload/v1591005850/sample.jpg'])
    f1.close()

'''
def f2():
    f2 = automation.FacebookInstance(username='@gmail.com',password='', temp_user_data=True)
    f2.login()
    f2.post_to_page(page_url='https://mobile.facebook.com/1322105514589118', content='post2', arr_images=['z:\\1.jpg'])
    f2.close()

def f3():
    f3 = automation.FacebookInstance(username='@gmail.com',password='', temp_user_data=True)
    f3.login()
    f3.post_to_page(page_url='https://mobile.facebook.com/1322105514589118', content='post3', arr_images=['https://res.cloudinary.com/minty/image/upload/v1591005850/sample.jpg'])
    f3.close()

def f4():
    f4 = automation.FacebookInstance(username='@gmail.com',password='', temp_user_data=True)
    f4.login()
    f4.post_to_page(page_url='https://mobile.facebook.com/1322105514589118', content='post4', arr_images=['z:\\1.jpg','z:\\1.jpg'])
    f4.close()
'''

#_thread.start_new_thread( f1 , ())
f1()

