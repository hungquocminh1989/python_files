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
import json, requests, pycurl, certifi
from datetime import datetime
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
            result = self.curl_1("POST", api_url, data)
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
            
            return requests.post(url, headers, data).json()
        
        elif method == "GET":
            
            return requests.get(url + "?" + field, headers).json()


    def curl_1(self, method, url, data):
        crl = pycurl.Curl()
        crl.setopt(crl.CAINFO, certifi.where())
        pf = urlencode(data)
        
        if method == "POST":
            crl.setopt(crl.URL, url)
            crl.setopt(crl.POSTFIELDS, pf)
        elif method == "GET":
            crl.setopt(crl.URL, url + "?" + pf)
        r = crl.perform_rs()
        r = json.loads(r)
        crl.close()
        return r



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
        result = self.curl_1("POST", api_url, data)
        print(photo_url)
        print(result)

        return result

    def execute_import(self):
    	pass

#Start application
token = "EAASp3DPmNo8BALQJmTNSRWZByePLQTveZAYkULNZCKOoDDVJS1EcnhtlZC9zCRH2ESr8ApVULYyETBC94GCyi4ftJqrkqX0H8f3RvZA1MyHHUcOA5tIArVqoZAjZAT255ZBezi2V4F2uw6Fb1wAj3OfyIaFZAp9tS9BxJYgJQ06mhzmk4YyqyqUzZCJVp3U4MgPPXeybopdQhZBqQZDZD"
folder_product_files = "C:\\Users"
folder_page_files = "C:\\Users"
attachments = [
    "https://www.donghogiarehcm.com/wp-content/uploads/2019/10/11612642516_75796048-300x300.jpg",
    "https://www.donghogiarehcm.com/wp-content/uploads/2019/10/11545581316_75796048-300x300.jpg",
]
tool = ImportPostTool(folder_product_files)
tool.create_page_post_api("2056902877684409", datetime.now().strftime('%Y%m%d%H%M%S%f'), attachments, token)
#tool.upload_photo_api("https://www.donghogiarehcm.com/wp-content/uploads/2019/10/11612642516_75796048-300x300.jpg", token)
exit()
