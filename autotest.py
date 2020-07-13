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
import sys, os, json
from datetime import datetime
from urllib.parse import urlencode

#Import lib common
sys.path.append('lib')
import common

class autotest:
    def __init__(self):
        self.shared = common.Shared()
        self.vultr = common.VultrInstance('')
        #self.remoting = common.Remoting("149.28.147.3", 15, "root", "")
    def run(self):
        r = self.vultr.create_server()
        info = self.vultr.get_server_info(r['SUBID'])
        #print(info)
        proxy = common.Proxy(hostname=info['main_ip'], password=info["default_password"])
        proxy.start()
        #self.vultr.destroy_server('38784580')
        #self.vultr.get_startupscript_list()
        '''
        commands = [
            'cd /home/minh/public_html',
            'ls',
            'php -v'
        ]
        '''
        #self.remoting.upload_file('credentials.json', "/home/minh/public_html")
        #self.remoting.upload_folder(os.getcwd() + '\\selenium' ,"/home/minh/public_html")
        #print(os.getcwd())
        

obj = autotest()
obj.run()
exit
