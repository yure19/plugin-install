#!/usr/bin/env python3

# USAGE:
#     $ MOZ_HEADLESS=1 python3 install.py url user password

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import sys
import shutil
import os
import time

URL = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
FIREFOX_BINARY_PATH = '/usr/bin/firefox'
EXECUTABLE_PATH = SCRIPT_DIRECTORY +  '/geckodriver-v0.26.0-linux64/geckodriver'
ZIP_FILES_PATH = SCRIPT_DIRECTORY + '/../installer/smsapi'
AMODULE_URL = URL + '/module'

USERNAME_INPUT_SELECTOR = '#emails'
PASSWORD_INPUT_SELECTOR = '#password'
SIGN_IN_BUTTON_SELECTOR = '#login-button'
TOOLS_LINK_SELECTOR = '#slide-out > ul > li:nth-child(10) > a'
MODULE_MANAGER_LINK_SELECTOR = 'a[href="amodule"]'
INSTALL_BUTTON_SELECTOR = '.waves-effect.waves-light.btn.green.darken-4.white-text'
UPLOAD_FILE_INPUT_SELECTOR = '#files'
UPLOAD_BUTTON_SELECTOR = '#mod-button'
CONFIRM_BUTTON_SELECTOR = '.confirm'
MARK_MODULE_LABEL_SELECTOR = '.responsive-table.bordered > tbody > tr > td:nth-child(1) > label'
WITH_SELECTED_LINK_SELECTOR = 'a[data-activates="bulka"]'
ENABLE_MODULE_LINK_SELECTOR = '#bulka > li:nth-child(2) > a'

driver = webdriver.Firefox(
    firefox_binary=FirefoxBinary(FIREFOX_BINARY_PATH), 
    executable_path=EXECUTABLE_PATH
)

driver.get(URL)

username_input = driver.find_element_by_css_selector(USERNAME_INPUT_SELECTOR)
username_input.send_keys(USERNAME)

password_input = driver.find_element_by_css_selector(PASSWORD_INPUT_SELECTOR)
password_input.send_keys(PASSWORD)

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, SIGN_IN_BUTTON_SELECTOR))).click()

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, TOOLS_LINK_SELECTOR))).click()

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, MODULE_MANAGER_LINK_SELECTOR))).click()

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, INSTALL_BUTTON_SELECTOR))).click()

zip_archive = shutil.make_archive(SCRIPT_DIRECTORY + '/flowroute', 'zip', ZIP_FILES_PATH)
upload_file_input = driver.find_element_by_css_selector(UPLOAD_FILE_INPUT_SELECTOR)
upload_file_input.send_keys(zip_archive)

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, UPLOAD_BUTTON_SELECTOR))).click()

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, CONFIRM_BUTTON_SELECTOR))).click()

driver.get(AMODULE_URL)

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, MARK_MODULE_LABEL_SELECTOR))).click()

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, WITH_SELECTED_LINK_SELECTOR))).click()

WebDriverWait(driver, 90).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ENABLE_MODULE_LINK_SELECTOR))).click()

driver.switch_to_alert().accept()

driver.get(AMODULE_URL)

os.remove(zip_archive)

driver.quit()
