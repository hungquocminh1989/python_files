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
import sys, os, json, requests, pycurl, certifi, xlrd, re
from datetime import datetime
from urllib.parse import urlencode
from pandas import *
from woocommerce import API

#Import lib common
sys.path.append('lib')
import common

class ImportPostTool:
    def __init__(self):
        command_line_arguments = sys.argv
        self.token = command_line_arguments[1] if len(sys.argv) > 1 else ''
        self.wcapi = API(
            url="https://koolwatch.me",
            consumer_key="ck_1c3ad135042991666c034cd0574bb4e1d85325b6",
            consumer_secret="cs_217afc1d1781b772f39087b0c983d9f1046fd014",
            wp_api=True,
            version="wc/v3",
            timeout=999999
        )
        self.number_post_fetch = 20
        self.product_per_page = 100 #100 is maximum
        self.category_men_suggest_arr = ['đồng hồ nam', 'dong ho nam', 'nam']
        self.category_women_suggest_arr = ['đồng hồ nữ', 'dong ho nu', 'nữ', 'nu']
        self.category_men_name = 'Đồng Hồ Nam' #Danh mục đồng hồ nam
        self.category_women_name = 'Đông Hồ Nữ' #Danh mục đồng hồ nữ
        self.categogry_uncategorized = 'Uncategorized' #Danh mục không xác định
        self.shared = curllib.Shared()

    def get_token_info_api(self, token):

        api_url = 'https://graph.facebook.com/v2.10/me'

        data = {
            "access_token" : token,
            'fields' : 'id,name',
        }

        result = self.shared.curl("GET", api_url, data)
        
        return result

    def get_page_post_api(self, page_id, limit, token):
        api_url = 'https://graph.facebook.com/v2.10/{0}/feed'.format(page_id)
        print(api_url)
        data = {
            "access_token" : token,
            'fields' : 'created_time,message,attachments,permalink_url',
            'limit' : limit,
        }
        result = self.shared.curl("GET", api_url, data)

        return result

    def get_list_wc_product(self):
        products = []

        #Get products
        iPage = 1
        products_for_page = self.wcapi.get("products", params={"page": iPage, "per_page": self.product_per_page}).json()

        while len(products_for_page) > 0:
            
            #Merge product all page
            products = products + products_for_page

            #Get next page
            iPage += 1
            products_for_page = self.wcapi.get("products", params={"page": iPage, "per_page": self.product_per_page}).json()

        return products

    def compare_product_exits(self, products, item_post):
        if len(products) > 0:
            for product in products:
                if len(product['meta_data']) > 0:
                    for metadata in product['meta_data']:
                        if metadata['key'] == '_fb_page_post_id':
                            if metadata['value'] == item_post['id']:
                                return True
                
        return False

    def detect_category_name(self, post_content):
        
        post_string = str.lower(post_content)

        #Check đồng hồ nam
        for item_str in self.category_men_suggest_arr:
            search = re.search(str.lower(item_str), post_string)
            if search != None:
                return self.category_men_name

        #Check đồng hồ nữ
        for item_str in self.category_women_suggest_arr:
            search = re.search(str.lower(item_str), post_string)
            if search != None:
                return self.category_women_name

        return self.categogry_uncategorized

    def create_wc_category(self, category_name):

        data_search = {
            "page": 1,
            "per_page": 100,
            "search": category_name,
        }
    
        result_ctg = self.wcapi.get("products/categories", params = data_search).json()

        if len(result_ctg) > 0:
            
            return result_ctg[0]['id']
        
        else:

            data = {
                "name": category_name,
            }

            result = self.wcapi.post("products/categories", data).json()
            
            return result['id']

    def create_wc_post(self, item_post):

        images = self.export_data_images(item_post)

        category_name = self.detect_category_name(item_post['message'])

        category_id = self.create_wc_category(category_name)
        
        data = {
            "name": "Auto product {0}".format(datetime.now().strftime('%Y%m%d%H%M%S%f')),
            "type": "simple",
            "status": "draft",
            "description": item_post['message'] + "\r\n" + "No.: " + item_post['id'],
            "meta_data": [
                {
                  "key": '_fb_page_post_id',
                  "value": item_post['id'],
                }
            ],
            "images": images,
            "categories": [
                {
                    "id": category_id,
                }
            ],
        }
        self.wcapi.post("products", data)

    def export_data_images(self, item_post):
        images = []
        for img in item_post['attachments']['data'][0]['subattachments']['data']:
            img_src = img['media']['image']['src']
            images.append({'src': img_src})
            #break

        return images
        

    def execute_import(self):
        token_info = self.get_token_info_api(self.token)
        if len(token_info) > 0:
            page_name = token_info['name']
            page_id = token_info['id']

            print('Page Name : ' + page_name)
            print('Page Id : ' + page_id)

            #List wordpress products
            products = self.get_list_wc_product()
            print('Number products on website : {0}'.format(len(products)))
            
            #List post
            posts = self.get_page_post_api(page_id, self.number_post_fetch, self.token)
            #print(posts['data'][0]['attachments']['data'][0]['subattachments']['data'][0]['media']['image']['src'])
            #exit()

            if len(posts['data']) > 0:
                print('Number post on facebook page : {0}'.format(len(posts['data'])))
                for page_post in posts['data']:
                    #page_post_id = page_post['id']
                    #page_post_permalink_url = page_post['permalink_url']
                    #page_post_content = page_post['message']
                    
                    status = self.compare_product_exits(products, page_post)

                    if status == False:
                        self.create_wc_post(page_post)
                        print('Đã đồng bộ 1 sản phẩm')
                    else:
                        print('Sản phẩm đã tồn tại')
            
#Start application
tool = ImportPostTool()
tool.execute_import()
exit()
