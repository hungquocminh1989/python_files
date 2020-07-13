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

class Shared:
    def curl(self, method, url, data = None, headers = None):

        crl = pycurl.Curl()

        crl.setopt(crl.CAINFO, certifi.where())

        if headers != None:
            crl.setopt(crl.HTTPHEADER, headers)

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
                if "?" in url:
                    #True
                    crl.setopt(crl.URL, url + "&" + postfields)
                else:
                    #False
                    crl.setopt(crl.URL, url + "?" + postfields)
            else:
                crl.setopt(crl.URL, url)

        result = crl.perform_rs()

        crl.close()
        
        try:
            result = json.loads(result)
        except ValueError as e:
            print(result)
        #print('Response info : ')
        #print(result)

        return result

#Import packages
import pysftp
from base64 import decodebytes
#import paramiko

class Remoting:

    def __init__(self, Hostname, Port, Username, Password):
        self.myHostname = Hostname
        self.myPort = Port
        self.myUsername = Username
        self.myPassword = Password
        self.myCnopts = pysftp.CnOpts(knownhosts='known_hosts')
        self.myCnopts.hostkeys = None

        #Get connect
        self.sftp = pysftp.Connection(
            host=self.myHostname,
            username=self.myUsername,
            password=self.myPassword,
            #private_key="id_rsa",
            port=self.myPort,
            cnopts=self.myCnopts
        )
        print("Connection succesfully stablished ... ")
        

    def upload_file(self, local_file, remote_directory):
        self.sftp.put(local_file, remote_directory)
        print("Put to a remote directory : {0}".format(local_file))
        
        return True

    def upload_folder(self, local_folder, remote_directory):
        self.sftp.put_d(local_folder, remote_directory)
        print("Put to a remote directory : {0}".format(local_folder))
        
        return True

    def execute_command(self, commands = []):

        print("Execute command ... ")
        for command in commands:
            r = self.sftp.execute(command)
            print(r)
            
        return True

    def close_connection(self):
        self.sftp.close()

        return True

import subprocess, requests
import winreg
class Proxy:
    def __init__(self, hostname, password, port="22", username="root"):
        self.connection = subprocess.Popen(["lib\\ssh_tool\\ConnectSSH.exe", hostname, port, username, password])
        print(self.connection)
        self.internet_settings = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                0,
                winreg.KEY_ALL_ACCESS
        )

    def start(self):
        retry_status = True
        retry_time = 0
        while retry_status:
            retry_time += 1
            try:
                print("Retry connection : {0} ...".format(retry_time))
                retry_status = False
                headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                proxies = {
                    'http': "socks5://127.0.0.1:1080",
                    'https': "socks5://127.0.0.1:1080"
                }
                r = requests.get('https://api.ipify.org/',proxies=proxies, headers=headers).content
                print(r)
            except:
                retry_status = True

        #self.apply_proxy_setting()
        print('Proxy connected.')

    def stop(self):
        self.connection.kill()
        #self.remove_proxy_setting()
        print('Proxy disconnected.')

    
    def apply_proxy_setting(self):
        self.set_key('ProxyEnable', 1)
        #self.set_key('ProxyOverride', u'*.local;<local>')  # Bypass the proxy for localhost
        self.set_key('ProxyServer', u'socks=127.0.0.1:1080')
        self.restart_explorer()

    def restart_explorer(self):
        run = subprocess.Popen(["taskkill", "/f", "/im", "explorer.exe"])
        run.wait()
        run = subprocess.Popen(["C:\\Windows\\explorer.exe"])
        #run.wait()

    def set_key(self, name, value):
        _, reg_type = winreg.QueryValueEx(self.internet_settings, name)
        winreg.SetValueEx(self.internet_settings, name, 0, reg_type, value)

    def remove_proxy_setting(self):
        self.set_key('ProxyEnable', 0)
        self.restart_explorer()
    

class VultrInstance:
    
    def __init__(self, api_key):
        self.shared = Shared()
        self.headers = ['API-Key:{0}'.format(api_key)]

    def create_server(self):
        
        data = {
            #https://api.vultr.com/v1/regions/list
            'DCID' : '40', #Sing
            
            #https://api.vultr.com/v1/plans/list
            'VPSPLANID' : '201', #5.00$

            #https://api.vultr.com/v1/os/list
            'OSID' : '167', #CentOS 7
            #'OSID' : '164', #Snapshot

            'label' : 'AutoCreate_{0}'.format(datetime.now().strftime('%Y%m%d%H%M%S%f')),

            #https://api.vultr.com/v1/snapshot/list
            #'SNAPSHOTID' : 'f235ea527177d',

            #https://api.vultr.com/v1/startupscript/list
            #'SCRIPTID' : '729601' #Install Python 3.8
        }

        #https://www.vultr.com/api/#server_create
        result = self.shared.curl('POST', 'https://api.vultr.com/v1/server/create', data, self.headers)
        print(result)
        
        return result

    def get_server_info(self, server_id = None):

        retry_status = True
        retry_time = 0
        while retry_status:
            
            if retry_time > 0:
                print("Retry get server info : {0} ...".format(retry_time))
            
            #https://www.vultr.com/api/#server_server_list
            result = self.shared.curl('GET', 'https://api.vultr.com/v1/server/list', None, self.headers)
            
            retry_time += 1

            if server_id != None:
                result = result[server_id]
                if result['default_password'] != 'not supported' and result['main_ip'] != '0.0.0.0':
                    retry_status = False
            else:
                retry_status = False

        print(result)

        return result

    def destroy_server(self, server_id):

        data = {
            'SUBID' : server_id
        }

        #https://www.vultr.com/api/#server_destroy
        #No response, check HTTP result code.
        self.shared.curl('POST', 'https://api.vultr.com/v1/server/destroy', data, self.headers)

        return True

    def start(self, server_id):

        data = {
            'SUBID' : server_id
        }

        #https://www.vultr.com/api/#server_start
        #No response, check HTTP result code.
        self.shared.curl('POST', 'https://api.vultr.com/v1/server/start', data, self.headers)

        return True

    def reboot(self, server_id):

        data = {
            'SUBID' : server_id
        }

        #https://www.vultr.com/api/#server_reboot
        #No response, check HTTP result code.
        self.shared.curl('POST', 'https://api.vultr.com/v1/server/reboot', data, self.headers)

        return True

    def get_startupscript_list(self):
        #https://www.vultr.com/api/#startupscript_startupscript_list
        result = self.shared.curl('GET', 'https://api.vultr.com/v1/startupscript/list', None, self.headers)
        print(result)
        return result
        

        
