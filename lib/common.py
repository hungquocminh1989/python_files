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

    def __init__(self, hostname, port, username, password):
        self.myHostname = hostname
        self.myPort = port
        self.myUsername = username
        self.myPassword = password
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
class ProxyX:
    def __init__(self, hostname, password, port="22", username="root", setting_proxy=False):
        self.connection = subprocess.Popen(["lib\\ssh_tool\\ConnectSSH.exe", hostname, port, username, password])
        print(self.connection)
        self.internet_settings = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                0,
                winreg.KEY_ALL_ACCESS
        )
        self.setting_proxy = setting_proxy

    def start(self):
        retry_status = True
        retry_time = 0
        while retry_status:
            
            try:
                
                if retry_time > 0:
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
                retry_time += 1
                retry_status = True

        if self.setting_proxy == True:
            self.apply_proxy_setting()
            
        print('Proxy connected.')

    def stop(self):
        self.connection.kill()

        if self.setting_proxy == True:
            self.remove_proxy_setting()
            
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

        if api_key == '':
            print('API-Key missing.')
            sys.exit()
        
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

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle, time
class SeleniumInstance:

    def __init__(self, proxy_mode = False, proxy_ip='127.0.0.1', proxy_port='1080'):
        
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        prefs = {
                "download.default_directory" : "C:\\SeleniumDownloads"
        }
        chrome_options.add_experimental_option("prefs",prefs)
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--disable-infobars")
        #chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']); # Hide display "Chrome is being controlled by automated test software"
        #chrome_options.add_extension('lib\\selenium\\chrome\\extensions\\swapmycookies.crx')

        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = "socks5://{0}:{1}".format(proxy_ip, proxy_port)
        #prox.socks_proxy = ""
        prox.ssl_proxy = "socks5://{0}:{1}".format(proxy_ip, proxy_port)

        capabilities = webdriver.DesiredCapabilities.CHROME

        #Pass check
        #Your connection is not private 
        #Attackers might be trying to steal your information from 1.1.1.1 (for example, passwords, messages, or credit cards). Learn more"
        capabilities['acceptSslCerts'] = True
        
        if proxy_mode == True :
            prox.add_to_capabilities(capabilities)
        
        self.webdriver = webdriver.Chrome(executable_path='lib\\selenium\\chrome\\driver\\chromedriver.exe', chrome_options=chrome_options, desired_capabilities=capabilities)
        self.time_sleep_waiting = 0.5 #seconds
        self.timeout_waiting = 30 #seconds
        
        #Implicit wait là khoảng thời gian chờ khi không tìm thấy đối tượng trên web (Apply cho toàn bộ đối tượng web)
        self.webdriver.implicitly_wait(self.timeout_waiting) #seconds

    def set_time_sleep_waiting(self, seconds):
        self.time_sleep_waiting = seconds
    
    def set_timeout_waiting(self, seconds):
        self.timeout_waiting = seconds
        #Implicit wait là khoảng thời gian chờ khi không tìm thấy đối tượng trên web (Apply cho toàn bộ đối tượng web)
        self.webdriver.implicitly_wait(self.timeout_waiting) #seconds

    def action_redirect(self, url):
        self.action_waiting() #default waiting
        self.webdriver.get(url)

    def action_waiting(self, seconds=None):
        if seconds == None :
            time.sleep(self.time_sleep_waiting)
        else:
            time.sleep(seconds)

    def action_input_text(self, xpath, value = ''):
        self.action_waiting() #default waiting
        el = self._find_by_xpath(xpath)
        el.send_keys(value)
        
        return el

    def action_input_combobox(self, xpath, value='', text=''):
        self.action_waiting() #default waiting
        el = self._find_by_xpath(xpath)
        select = Select(el)

        if value != '':
            select.select_by_value(value)
        elif text != '':
            select.select_by_visible_text(text)

        return el

    def action_input_tap(self, xpath):
        self.action_waiting() #default waiting
        el = self.get_control(xpath)
        touchactions = TouchActions(self.webdriver)
        touchactions.double_tap(el)
        
        return el

    def action_input_click(self, xpath):
        self.action_waiting() #default waiting
        el = self.get_control(xpath)
        el.click()
        
        return el

    def get_control(self, xpath):
        el = self._find_by_xpath(xpath)

        return el

    def _find_by_xpath(self, xpath):
        
        el = None
        retry_status = True
        retry_time = 0
        while retry_status:
            try:
                if retry_time > 0:
                    print("Retry find element {0} : {1} ...".format(xpath, retry_time))
                    
                #el = self.webdriver.find_element_by_xpath(xpath)

                el = WebDriverWait(self.webdriver, self.timeout_waiting, poll_frequency=1).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                            
                retry_status = False
                
            except:
                print('XPATH : {0} Not found.'.format(xpath))
                retry_time += 1
                #self.close()
                #sys.exit()

        return el

    def action_input_enter(self, element):
        self.action_waiting() #default waiting
        element.send_keys(Keys.RETURN)

        return element
    
    '''
    def save_cookies(self, filepath):
        pickle.dump(self.webdriver.get_cookies(), open(filepath,"wb"))#file.pkl

        return True

    def load_cookies(self, filepath):
        cookies = pickle.load(open(filepath, "rb"))#file.pkl
        for cookie in cookies:
            self.webdriver.add_cookie(cookie)

        return True
    '''

    def close(self):
        self.webdriver.close()
        self.webdriver.quit()

'''
#Chưa test
#pip install python-crontab
from crontab import CronTab
class CronSetting:

    def __init__(self, username):
        self.my_cron = CronTab(user=username)

    def addCommand(self, command, comment):
        self.my_cron.new(command=command, comment=comment)
        
        return None

    def updateSchedule(self, comment):
        for job in self.my_cron:
            if job.comment == comment:
                job.minute.every(1)

        self.write()

        return None

    def remove(self, comment):
        self.my_cron.remove(comment=comment)
        self.write()

        return None

    def write(self):
        self.my_cron.write()
        self.my_cron.enable()
        self.my_cron.every_reboot()

        return None
'''

    
        

        
