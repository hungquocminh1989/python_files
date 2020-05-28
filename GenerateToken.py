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

class ImportPostTool:
    def __init__(self):
        command_line_arguments = sys.argv
        self.token = command_line_arguments[1] if len(sys.argv) > 1 else 'EAASp3DPmNo8BAJANUw4ZCQYxN3ZCgMZA7juy8T2DEQVIZCZC4jCzTesTrXddbV9puNVAwnkyibbSrBxCOTloPZAz7JXHFzOM2WgPPXL38aparrI7k8EgAFZCDdVSSZAflYL7aghaVOF3h4FewoHg8VvrK9SYXAQmdUmTVh6LFLZA8hJFTmOuldffuZB6R4Tpi1g28ZD'
        self.page_id = command_line_arguments[2] if len(sys.argv) > 1 else '1042724125855991'
        self.client_id = "1312663135467151'
	self.client_secret = "d755242eafec2782d22b5dcb42d3a794"

    def curl(self, method, url, data):

        crl = pycurl.Curl()

        crl.setopt(crl.CAINFO, certifi.where())

        #print('Post data : ')
        #print(data)
        
        postfields = urlencode(data) if data != None else None
        
        if method == "POST":

            crl.setopt(crl.URL, url)

            crl.setopt(crl.POSTFIELDS, postfields)

        elif method == "DELETE":

            crl.setopt(crl.URL, url)

            crl.setopt(crl.POSTFIELDS, postfields)

            crl.setopt(crl.CUSTOMREQUEST, 'DELETE')

        elif method == "GET":

            if postfields != None:
                crl.setopt(crl.URL, url + "?" + postfields)
            else:
                crl.setopt(crl.URL, url)

        result = crl.perform_rs()

        crl.close()

        result = json.loads(result)
        print('Response info : ')
        print(result)
        
        return result

    def generate_token(self):
        api_url = 'https://graph.facebook.com/v6.0/oauth/access_token?grant_type=fb_exchange_token&client_id={0}&client_secret={1}&fb_exchange_token={2}'.format(self.client_id, self.client_secret, self.token)
        result = self.curl("GET", api_url, None)
        access_token = result['access_token']

	api_url = 'https://graph.facebook.com/v6.0/{0}/accounts?access_token={1}'.format(self.page_id, access_token)
	result = self.curl("GET", api_url, None)
        page_access_token = result['access_token']
        print(page_access_token)
    
        
            
#Start application
tool = ImportPostTool()
tool.generate_token()
exit()
