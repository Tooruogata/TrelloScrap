# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:05:02 2020

Title: Trello json/txt - Scrap

@author: tooru
"""

'''
Preamble
'''
import os
import requests
import json
import pandas as pd
import urllib
from os.path import isfile, join
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

'''
0) Setting
'''
#Set trello's user and password
user = 'insert the mail you want to use'
password = 'insert the passwortd'

#Set webdriver path 
wd_path = 'define selenium chrome driver executable'

#Download path
path = 'insert working directory'
os.chdir(path)

#List of id url in Trello
list_url =     ['XXXXXXX']

#Set Webdriver and WebDriverWait
driver = webdriver.Chrome(wd_path)
wait = WebDriverWait(driver, 30)

'''
1) Login to trello
'''

#Get the trello login webpage
driver.get("https://trello.com/login")

# save mainwindow
main_window = driver.current_window_handle

#Wait until login click is available
wait.until(EC.presence_of_element_located((By.ID, "login")))

#Send keys for user and password
time.sleep(5)
driver.find_element_by_id('user').send_keys(user)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('login').click()


print('First login')

#Wait until login-submit click is available
time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID, "login-submit")))

time.sleep(5)
#Send keys for password
driver.find_element_by_id('password').send_keys(password)
time.sleep(5)
driver.find_element_by_id('login-submit').click()

print('Second login')

#Wait until banners is available as a proxy to download 
wait.until(EC.presence_of_element_located((By.ID, "banners")))
time.sleep(5)

print('-----------Ready to download-----------')

'''
Sec download
'''

a = 0
for url in list_url:
    a = a + 1
    driver.execute_script("window.open('https://trello.com/b/" + url + ".json');")
    driver.switch_to.window(driver.window_handles[a])
    temp = driver.find_element_by_xpath(r'/html/body').text

    text_file = open(url + '.txt', "w", encoding = 'utf-8-sig')
    text_file.write(temp)
    text_file.close()
    print('Download #' + str(a))

    
