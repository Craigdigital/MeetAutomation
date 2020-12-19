from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import argparse
from getpass import getpass

PATH = 'geckodriver.exe'

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("intl.accept_languages", "en-us")
firefox_profile.set_preference("permissions.default.microphone", 1)
firefox_profile.set_preference("permissions.default.camera", 1)

driver = webdriver.Firefox(
    executable_path=PATH, firefox_profile=firefox_profile)
wait = WebDriverWait(driver, 10