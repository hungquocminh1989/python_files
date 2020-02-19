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
import json, requests
from urllib.parse import urlencode

class ImportPostTool:
    def __init__(self, folder_product_files):
        pass

    def read_product_excel(self):
        pass

    def read_page_excel(self):
        pass

    def create_page_post_api(self, page_id, message, attachments, token):

        api_url = "https://graph.facebook.com/v2.10/{0}/feed".format(page_id)
        
        data = {
            "message" : message,
            "access_token" : token,
        }
        
        media_fbid = self.upload_multi_photo(attachments, token)

        if len(media_fbid) > 0:
            data = {**data, **media_fbid}
            print(data) 
            result = self.curl("POST", api_url, data)
            print(result)
            return result
            
        return None

    def upload_multi_photo(self, attachments, token):
        media_fbid = {}

        if len(attachments) > 0:
            for i in range(len(attachments)):
                r = self.upload_photo_api(photo_url=attachments[i], token=token)
                if len(r) > 0 and r["id"] != "":
                    media_fbid["attached_media[{0}]".format(i)] = "{'media_fbid':'"+r["id"]+"'}"

        print(media_fbid)    
        return media_fbid

    def curl(self, method, url, data):
        
        field = urlencode(data)
        
        headers = {}
        
        if method == "POST":
            
            return requests.post(url, headers, data, verify=False).json()
        
        elif method == "GET":
            
            return requests.get(url + "?" + field, headers).json()

        

    def upload_photo_api(self, photo_url, token):
        
        #Upload photo unPublished
        data = {
            "url" : photo_url,
            "published" : False,
            "access_token" : token
        }

        # Param input :
        # [url] 
        # [published] = false
        api_url = 'https://graph.facebook.com/v2.10/me/photos'
        result = self.curl("POST", api_url, data)
        print(photo_url)
        print(result)

        return result

    def execute_import(self):
        pass

#Start application
folder_product_files = "C:\\Users"
folder_page_files = "C:\\Users"
attachments = ["https://13.231.155.63/img/dummy.png", "https://www.lixil-sashdoor.jp/mitsumori-system/estimate/img/icon/h_logo.png"]
tool = ImportPostTool(folder_product_files)
tool.create_page_post_api("2056902877684409", "test11112222", attachments, "EAASp3DPmNo8BAAfXGyC5rvZAjNdbeH5s2W7HvPpeAM412bDzcr2fZAmMA2cAXlrHD8kZAlT5xAlGJUaR5HB8t3atnSKLJnSRI4Gy9HlVkH7480gHviao3k2li8BMRMZAsbghy7TNuVrQEI6PGUStRJRLQYL6AKbDfZBRKlcpBcTUpbGniQYC8RhoQuvV2Qw9TFHNNbz6BEQZDZD")
exit()
