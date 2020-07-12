#!/usr/bin/env python
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
"""

#Import lib
from selenium import webdriver

browser = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')
browser.get('http://seleniumhq.org/')

exit()
