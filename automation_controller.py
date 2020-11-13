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
import os, sys

#Import lib common
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOT_DIR + '/lib')
import common, automation

f1 = automation.FacebookInstance(username='',password='')
f1.login()
f1.post_to_page(page_url='https://mobile.facebook.com/1322105514589118', content='test', arr_images=['https://res.cloudinary.com/minty/image/upload/v1591005850/sample.jpg'])
f1.post_to_page(page_url='https://mobile.facebook.com/209702559749142', content='test', arr_images=['https://res.cloudinary.com/minty/image/upload/v1591005850/sample.jpg'])
f1.close()
