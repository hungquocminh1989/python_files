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
import json, requests, pycurl, certifi, xlrd
from datetime import datetime
from urllib.parse import urlencode
from pandas import *

class ImportPostTool:
    def __init__(self):
        self.import_excel_files = 'C:\\Users\\QuocMinh\\Desktop\\python_files\\wp_product.xlsx'

    def read_excel_import(self):
        dict_excel = {}
        xls = ExcelFile(self.import_excel_files)
        sheet_product = xls.parse(xls.sheet_names[0])
        sheet_page = xls.parse(xls.sheet_names[1])
        
        dict_excel['sheet_product'] = sheet_product.to_dict()
        dict_excel['sheet_page'] = sheet_page.to_dict()
        
        return dict_excel

    def upload_multi_photo(self, attachments, token):
        media_fbid = {}

        if len(attachments) > 0:
            for i in range(len(attachments)):
                r = self.upload_photo_api(photo_url=attachments[i], token=token)
                if len(r) > 0 and r["id"] != "":
                    media_fbid["attached_media[{0}]".format(i)] = "{'media_fbid':'"+r["id"]+"'}"
    
        return media_fbid

    def curl_requests(self, method, url, data):
        
        field = urlencode(data)
        
        headers = {}
        
        if method == "POST":
            
            return requests.post(url, headers, data).json()
        
        elif method == "GET":
            
            return requests.get(url + "?" + field, headers).json()

    def curl(self, method, url, data):

        crl = pycurl.Curl()

        crl.setopt(crl.CAINFO, certifi.where())

        postfields = urlencode(data)
        
        if method == "POST":

            crl.setopt(crl.URL, url)

            crl.setopt(crl.POSTFIELDS, postfields)

        elif method == "GET":

            crl.setopt(crl.URL, url + "?" + postfields)

        result = crl.perform_rs()

        crl.close()

        result = json.loads(result)

        return result

    def create_page_post_api(self, page_id, message, attachments, token):

        api_url = "https://graph.facebook.com/v2.10/{0}/feed".format(page_id)
        
        data = {
            "message" : message,
            "access_token" : token,
        }
        print(page_id)
        #print(token)
        #print(attachments)
        #print(message)
        media_fbid = self.upload_multi_photo(attachments, token)
        print(media_fbid)
        if len(media_fbid) > 0:

            #Merge data
            data = {**data, **media_fbid}

            result = self.curl("POST", api_url, data)
            print(result)
            return result
            
        return None

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

        return result

    def execute_import(self):
        dict_excel = self.read_excel_import()
        sheet_product = dict_excel['sheet_product']
        sheet_page = dict_excel['sheet_page']
        excel_product_row = len(sheet_product['No.'])
        excel_page_row = len(sheet_page['No.'])
        
        for excel_page_row in range(len(sheet_page['No.'])):
            print('-------')
            print(excel_page_row)
            page_name = sheet_page['Page Name'][excel_page_row].strip()
            page_id = str(sheet_page['Page Id'][excel_page_row]).strip()
            page_token = sheet_page['Token'][excel_page_row].strip()
            for excel_product_row in range(len(sheet_product['No.'])):
                product_name = sheet_product['Product Name'][excel_product_row].strip()
                product_content = sheet_product['Contents'][excel_product_row]
                product_images_list = sheet_product['Images'][excel_product_row].split('\n')

                #Post
                self.create_page_post_api(page_id, product_content, product_images_list, page_token)
                
                

#Start application
token = "EAASp3DPmNo8BAOST4eDlXXqlg3108Xo0QNZAbsEZALHi4jCZBgeowFOTons3RN5Cyx9TQeG2oR2fYLf4CmC3qzz4LvsOpb8aqXzcWaeVu7Xo8GdH5foopVinlstZAf2geXbZAKcO1FQZAhI1G0fYsyBaMls667PIZCIwoFn6ZAZBn0CVo8LSPFJHBC00djr87nZC9mdxAsqceiuAZDZD"
page_id = '1322105514589118'
folder_product_files = "C:\\Users"
folder_page_files = "C:\\Users"
attachments = [
    "https://www.donghogiarehcm.com/wp-content/uploads/2019/10/11612642516_75796048-300x300.jpg",
    "https://www.donghogiarehcm.com/wp-content/uploads/2019/10/11545581316_75796048-300x300.jpg",
]
tool = ImportPostTool()
tool.execute_import()
#tool.create_page_post_api(page_id, datetime.now().strftime('%Y%m%d%H%M%S%f'), attachments, token)
#tool.upload_photo_api("https://www.donghogiarehcm.com/wp-content/uploads/2019/10/11612642516_75796048-300x300.jpg", token)
exit()
