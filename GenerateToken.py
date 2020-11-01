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
import sys, os, json, requests, pycurl, certifi
from datetime import datetime
from urllib.parse import urlencode

#Import lib common
sys.path.append('lib')
import common

class GenerateTool:
    def __init__(self):
        command_line_arguments = sys.argv
        self.token = command_line_arguments[1] if len(sys.argv) > 1 else 'EAASp3DPmNo8BAKpntKz6dfpc6qxSIzU4CU26iADtiUJuS4RPI8lLKCht7YIZBddtm1g8oxEHe0t8D486nrPz2xi3Hqj2F69IaDwUwEZBzsaZC9RgRqeIgIi1iQ9K5ueAZAo9RyKu7Upg3qDqtems6Xc7INSFZBE6YWxDkYSOZAyaZBEZAVi950v2x9YllD0mLBwZD'
        self.page_ids_string = command_line_arguments[2] if len(sys.argv) > 1 else '1322105514589118'
        self.user_id = '2362323090677387' #Minh Hung
        self.client_id = "1312663135467151"
        self.client_secret = "d755242eafec2782d22b5dcb42d3a794"
        self.shared = common.Shared()

    def generate_token(self):
        api_url = 'https://graph.facebook.com/v6.0/oauth/access_token?grant_type=fb_exchange_token&client_id={0}&client_secret={1}&fb_exchange_token={2}'.format(self.client_id, self.client_secret, self.token)
        result = self.shared.curl("GET", api_url, None)
        access_token = result['access_token']

        api_url = 'https://graph.facebook.com/v6.0/{0}/accounts?access_token={1}'.format(self.user_id, access_token)
        result = self.shared.curl("GET", api_url, None)
        data = result['data']
        print(data)
        page_id_arr = self.page_ids_string.split(" ")
        for item in data:
            if item['id'] in page_id_arr or self.page_ids_string == None:
                print(item['id']  + ' - ' + item['name'] + ' - ' + item['access_token'])

#Start application
tool = GenerateTool()
tool.generate_token()
exit()
