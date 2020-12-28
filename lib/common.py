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
import sys, os, json, requests, pycurl, certifi, logging, configparser
from datetime import datetime
from urllib.parse import urlencode
from pathlib import Path
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__)).replace(os.sep, '/')

class Config:
    def load_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        return config

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

'''
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
'''
    

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
from selenium.webdriver.common.action_chains import ActionChains
import pickle, time, uuid, speedtest #https://pypi.org/project/speedtest-cli/
import psutil
import urllib.request
from contextlib import suppress
from pywinauto.application import Application #https://zakovinko.com/blog/2016/upload-files-with-selenium-windows-version/
from shutil import copyfile
from pathlib import Path

class SeleniumInstance:

    def __init__(self
                 , proxy_mode = False
                 , proxy_ip='127.0.0.1'
                 , proxy_port='1080'
                 , system_os = 'win'
                 , remote_url = ''
                 , session='_default'
                 , headless=False
                 , auto_detect_timeout=False
                 , dynamic_user_data = False
        ):
        
        #Define variable
        self.config = Config().load_config()
        SELENIUM_DEBUG_CONST = self.config['SELENIUM']['DEBUG_CONST']
        self.dblogs = DBLogs()
        self.expected_condition_type = 'element_to_be_clickable'
        self.auto_screenshot = False
        self.time_sleep_waiting = 1 #seconds
        self.timeout_waiting = 30 #seconds
        self.time_retry_setting = 2 #5 lần
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Create define variable')

        # Create base folder
        self.init_folder(session, dynamic_user_data)
        self.local_storage = {
            'download' : self.download_dir,
            'screenshot' : self.screenshot_dir,
        }

        # Check internet
        if(auto_detect_timeout==True):
            s = speedtest.Speedtest()
            s.get_best_server()
            s.download()
            self.timeout_waiting = round(s.results.ping)
            self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Detect internet speed : {self.timeout_waiting}')
            
        
        chrome_options = Options()
        #chrome_options.add_argument("--start-maximized")
        prefs = {
                "download.default_directory" : self.local_storage['download']
        }
        chrome_options.add_experimental_option("prefs",prefs)

        if(headless == True):
            chrome_options.add_argument('--headless')

        if(session != False):
            chrome_options.add_argument(f"user-data-dir={self.userdata_dir}") #Path to your chrome profile
        
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

        if system_os == 'win':
            selenium_driver = 'lib/selenium/chrome/driver/chromedriver.exe'
            self.autoit = AutoIT()
        elif system_os == 'linux':
            selenium_driver = 'lib/selenium/chrome/driver/chromedriver'
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
        else:
            selenium_driver = ''

        if remote_url == '':
            self.webdriver = webdriver.Chrome(executable_path=selenium_driver, chrome_options=chrome_options, desired_capabilities=capabilities)
        else:
            self.webdriver = webdriver.Remote(command_executor=f'{remote_url}/wd/hub', desired_capabilities=capabilities)
        
        #Implicit wait là khoảng thời gian chờ khi không tìm thấy đối tượng trên web (Apply cho toàn bộ đối tượng web)
        self.webdriver.implicitly_wait(self.timeout_waiting) #seconds
        self.current_window_handle = self.webdriver.current_window_handle
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Create selenium instance')

    def init_folder(self, session, dynamic_user_data):

        if session != False:
            
            # Define folder
            self.download_dir = f'{TMP_DIR}/Selenium_Storage/{session}/Downloads'
            self.screenshot_dir = f'{TMP_DIR}/Selenium_Storage/{session}/Screenshots'
            self.userdata_dir = f'{TMP_DIR}/Selenium_Storage/{session}/UserData'

            if dynamic_user_data == True:
                self.userdata_dir = f'{TMP_DIR}/Selenium_Storage/{session}/UserData_{self.dblogs.session_id}'

            # Create folder
            Path(self.download_dir).mkdir(parents=True, exist_ok=True)
            Path(self.screenshot_dir).mkdir(parents=True, exist_ok=True)
            Path(self.userdata_dir).mkdir(parents=True, exist_ok=True)

            self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Create init folder')

    def active_current_window(self):
        self.webdriver.switch_to_window(self.current_window_handle)
    
        return None

    def set_expected_condition_type(self, val):
        self.expected_condition_type = val

    def enable_auto_screenshot(self):
        self.auto_screenshot = True

    def set_time_retry_setting(self, time_number):
        self.time_retry_setting = time_number

    def set_time_sleep_waiting(self, seconds):
        self.time_sleep_waiting = seconds
    
    def set_timeout_waiting(self, seconds):
        self.timeout_waiting = seconds
        #Implicit wait là khoảng thời gian chờ khi không tìm thấy đối tượng trên web (Apply cho toàn bộ đối tượng web)
        self.webdriver.implicitly_wait(self.timeout_waiting) #seconds

    def action_download_file(self, url):
        ext_arr = Path(url).suffixes
        file_ext = ext_arr[len(ext_arr)-1]
        image_name='{0}{1}'.format(datetime.now().strftime('%Y%m%d_%H%M%S_%f'), file_ext)
        download_path = f"{self.local_storage['download']}/{image_name}"
        urllib.request.urlretrieve(url, download_path)

        return download_path

    def action_redirect(self, url):
        self.action_waiting() #default waiting
        self.webdriver.get(url)
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Redirect : {url}')

    def action_waiting(self, seconds=None):
        if seconds == None :
            time.sleep(self.time_sleep_waiting)
        else:
            time.sleep(seconds)

        if self.auto_screenshot == True:
            self.action_screenshot()

        self.active_current_window()

    def action_switch_to_iframe(self, xpath):
        self.webdriver.switch_to.default_content()
        self.webdriver.switch_to.frame(self.get_control(xpath))
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Switch to iframe : {xpath}')

    def action_switch_to_default(self):
        self.webdriver.switch_to.default_content()
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Switch to default content')

    def action_handle_alert_window(self):
        # .accept()
        # .dismiss()
        # .text
        
        return self.webdriver.switch_to.alert

    def action_input_text(self, xpath, value = ''):
        self.action_waiting() #default waiting
        el = self._find_by_xpath(xpath)
        el.send_keys(value)
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Add to a textbox : {value} - {xpath}')
        
        return el

    def action_input_combobox(self, xpath, value='', text=''):
        self.action_waiting() #default waiting
        el = self._find_by_xpath(xpath)
        select = Select(el)

        if value != '':
            select.select_by_value(value)
        elif text != '':
            select.select_by_visible_text(text)

        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Select a combobox : {value} - {xpath}')

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

        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Click to a button : {xpath}')
        
        return el

    def action_get_text(self, xpath):
        self.action_waiting() #default waiting
        el = self.get_control(xpath)
        return el.text

    def action_upload_file(self, xpath):
        self.action_waiting() #default waiting
        el = self.action_input_click(xpath)
        self.action_waiting() #default waiting
        el.send_keys(file)
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Click to a button upload file : {xpath}')

        return None

    def action_autoit_upload_file(self, xpath, file):

        file_exist = False

        file_check = Path(file)
        if file_check.is_file():
            self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Check exist file OK : {file}')
            file = file.replace('/', os.sep)
            file_exist = True
        elif requests.get(file).status_code == 200:
            self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Check exist url OK : {file}')
            file_exist = True
        
        if file_exist == True:
            self.action_waiting() #default waiting
            el = self.action_input_click(xpath)
            self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Click to a button upload file : {xpath}')
            self.action_waiting() #default waiting
            self.autoit.win_popup_select_file(file)
            self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Select file with AutoIT')

            return el

        return False

    def action_screenshot(self, image_name='', upload_mode=False):
        if image_name == '':
            image_name='{0}.png'.format(datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
            
        self.webdriver.save_screenshot("{0}/{1}".format(self.local_storage['screenshot'],image_name))
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Create a screenshot : {image_name}')

        
        if upload_mode == True:
            cloud = Cloudinary()
            cloud.upload("{0}/{1}".format(self.local_storage['screenshot'],image_name))
            self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Upload a screenshot : {image_name}')

            return ''

        return None

    def action_check_exist_element(self, xpath):
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Check exist element')
        el = self._find_by_xpath(xpath, check_exist=True)
        if el == False:
            return False

        return True


    def set_path_storage_screenshot(self, path_storage):
        self.local_storage['screenshot'] = path_storage

    def get_control(self, xpath):
        el = self._find_by_xpath(xpath)
        self.move_to_element(el)

        return el

    def move_to_element(self, el):
        actions = ActionChains(self.webdriver)
        actions.move_to_element(el).perform()
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Scroll to element')

        return el

    def _find_by_xpath(self, xpath, check_exist=False):
        
        el = None
        retry_status = True
        retry_time = 0
        while retry_status:
            try:
                if retry_time > 0:
                    print("Retry find element {0} : {1} ...".format(xpath, retry_time))
                    self.dblogs.debug_log(f"{SELENIUM_DEBUG_CONST}Retry find element {xpath} : {retry_time} ...")
                    
                #el = self.webdriver.find_element_by_xpath(xpath)

                # https://selenium-python.readthedocs.io/waits.html
                ec = eval('EC.{0}((By.XPATH, xpath))'.format(self.expected_condition_type))

                el = WebDriverWait(self.webdriver, self.timeout_waiting, poll_frequency=1).until(
                    ec
                )
                            
                retry_status = False
                
            except:                        
                
                print('XPATH : {0} Not found.'.format(xpath))
                self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}XPATH : {xpath} Not found')
                retry_time += 1

                if check_exist == True:
                    return False

                elif retry_time >= self.time_retry_setting:
                    self.close()
                    sys.exit()
                    self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Close program')

            finally:
                self.expected_condition_type = 'element_to_be_clickable'

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
        self.action_waiting(5)
        self.webdriver.close()
        self.webdriver.quit()
        self.dblogs.debug_log(f'{SELENIUM_DEBUG_CONST}Close program')

import cloudinary.uploader
class Cloudinary:
    
    def __init__(self, cloud_name, api_key, api_secret):
        self.cloudinary = cloudinary
        self.cloudinary.config( 
            cloud_name = cloud_name,
            api_key = api_key, 
            api_secret = api_secret 
        )

    def upload(self, url):
        result = self.cloudinary.uploader.upload(url)

        return result

    def destroy(self, public_id):
        result = self.cloudinary.uploader.destroy(public_id)

        return result

    def multi_upload(self, attachments):
        cloudinary_images = {}
        if len(attachments) > 0:
            for i in range(len(attachments)):
                result = self.upload(attachments[i])
                self.cloudinary_images[result['public_id']] = result['secure_url']

        return cloudinary_images

    def remove(self, cloudinary_urls):
        if len(cloudinary_urls) > 0:
            for public_id in cloudinary_urls:
                self.destroy(public_id)

        return None

import mysql.connector
class MySQL:

    def __init__(self, host, database, username, password, port=3306):
        self.connection = mysql.connector.connect(
            host=host,
            username=username,
            password=password,
            port=port,
            database=database,
        )
        self.db = self.connection.cursor()

    def query(self, sql, param=None):
        self.db.execute(sql, param)

        return self.db.fetchall()

    def execute(self, sql, param=None):
        self.db.execute(sql, param)
        self.connection.commit()
        
        return True

class DBLogs:
    def __init__(self, disable=False):
        self.config = Config().load_config()
        self.db = MySQL(self.config['MYSQL']['HOST'], self.config['MYSQL']['DB_NAME'], self.config['MYSQL']['USERNAME'], self.config['MYSQL']['PASSWORD'], self.config['MYSQL']['PORT'])
        self.disable = disable
        self.session_id = uuid.uuid4()

    def execute_log(self, execute_id='-1', message='', url=''):
        sql = f"""
            INSERT INTO t_execute_logs (t_execute_id, message, image_url)
            VALUE ('{execute_id}', '{message}', '{url}');
        """
        self.db.execute(sql)

        return None

    def debug_log(self, message=''):
        if self.disable == False:
            sql = f"""
                INSERT INTO t_debug_logs (session_id, message)
                VALUE ('{self.session_id}', '{message}');
            """
            self.db.execute(sql)

        return None

class Logs:
    def __init__(self, file_log='tmp.log'):
        self.logger = self.create_logger(file_log)

    def create_logger(self, file_log):

        #https://docs.python.org/3/library/logging.html#logging.Formatter
        asctime = '%(asctime)s'
        levelname = '%(levelname)s'
        pathname  = '%(pathname)s'
        lineno = '%(lineno)d'
        funcName = '%(funcName)s'
        message = '%(message)s'
        
        log_content_format = logging.Formatter(f'[{asctime}] - [{levelname}] - {message} - [ Function: {funcName}, Line: {lineno} , File: "{pathname}" ]')

        #Create main logger
        logger = logging.getLogger('main')

        #Create file handler
        file_handler = logging.FileHandler(f'{TMP_DIR}/{file_log}')
        file_handler.setFormatter(log_content_format)
        
        #Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_content_format)
        
        #Add handler
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        #Set logging level
        logger.setLevel(logging.DEBUG) # DEBUG < INFO < WARNING < ERROR < CRITICAL

        return logger

import pandas
class Excel:

    def __init__(self):
        self.excel = None

    def load(self, file):
        self.excel = pandas.ExcelFile(file)

        return None

    def get_sheet(self, sheetname):
        sheet = self.excel.parse(sheetname)

        return sheet

    def get_sheets(self):
        sheets= {}
        for sheet_name in self.excel.sheet_names:
            sheets[sheet_name] = self.get_sheet(sheet_name)

        return sheets

class ImportExcelToDB:

    def __init__(self):
        self.config = Config().load_config()
        self.db = MySQL(self.config['MYSQL']['HOST'], self.config['MYSQL']['DB_NAME'], self.config['MYSQL']['USERNAME'], self.config['MYSQL']['PASSWORD'], self.config['MYSQL']['PORT'])

    def import_master(self, file):
        xls = Excel()
        xls.load(file)
        sheets = xls.get_sheets()

        for tablename, rows in sheets.items():
            self.generate_sql_insert(tablename, rows)

        return None

    def generate_sql_insert(self, tablename, rows):
        # Truncate table
        self.db.execute(f"TRUNCATE TABLE {tablename};")

        # Insert table
        columns = rows.columns.values
        columns_name = ', '.join(columns)
        for row in rows.iterrows():
            list_values = []
            for col in columns:
                list_values.append(str(row[1][col]))

            columns_value = "'{0}'".format("', '".join(list_values))
            sql = f"""
                INSERT INTO {tablename} ({columns_name})
                VALUES ({columns_value});
            """
            print(sql)
            self.db.execute(sql)


        return None
        

import win32com.client
class AutoIT:
    def __init__(self):
        self.autoit = win32com.client.Dispatch("AutoItX3.Control")

    def win_popup_select_file(self, file):
        currenttext = ''
        self.autoit.WinSetState('Open','',self.autoit.SW_HIDE)
        self.autoit.WinActivate('Open')
        while currenttext != file or self.autoit.WinActive('Open') == 0:
            self.autoit.WinActivate('Open')
            self.autoit.WinWaitActive('Open')
            self.autoit.ControlSetText('Open','','[CLASS:Edit; INSTANCE:1]', file)
            currenttext = self.autoit.ControlGetText('Open','','[CLASS:Edit; INSTANCE:1]')
            
        while self.autoit.WinActive('Open') == 0:
            self.autoit.WinActivate('Open')
            
        self.autoit.ControlClick('Open','','[CLASS:Button; INSTANCE:1]')

        return None

class ExecuteAutomation:
    def __init__(self):
        self.config = Config().load_config()
        self.db = MySQL(self.config['MYSQL']['HOST'], self.config['MYSQL']['DB_NAME'], self.config['MYSQL']['USERNAME'], self.config['MYSQL']['PASSWORD'], self.config['MYSQL']['PORT'])

    def execute_queue(self):
        sql = """
            SELECT e.id, p.*
            FROM t_execute AS e
            INNER JOIN wp_product AS p
                ON e.wp_product_id = p.id
                    AND p.del_flg = 0
            WHERE e.del_flg = 0
                AND e.status = 0
            LIMIT 1
        """
        r = self.db.query(sql)

        return r

    def complete_queue(self, t_execute_id):

        sql = f"""
            UPDATE t_execute
            SET status = 9
            WHERE status = 1 AND id = {t_execute_id}
        """
        self.db.execute(sql)
        
        return None
        

        


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

    
        

        
