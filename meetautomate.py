
"""
AUTHOR: Maheswaran
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
import os
import time

PATH = "geckodriver.exe"

# firefox profiles
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("intl.accept_languages", "en-us")
firefox_profile.set_preference("permissions.default.microphone", 1)
firefox_profile.set_preference("permissions.default.camera", 1)

# driver declaration
driver = webdriver.Firefox(
    executable_path=PATH, firefox_profile=firefox_profile)

# WebDriverWait initialization
wait = WebDriverWait(driver, 10)

# authorization too google

# EMAIL
driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

try:
    search = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='identifierId']")))
except:
    print("Email locator failed")

email = "mahesh.official.1711@gmail.com"
password = "Nilap@1234"
meeting_id = "pqc-qosw-zag"
# mute_xpath = "//*[@id=yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span"
# video_xpath = "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div/div[1]"

time.sleep(2)

search.send_keys(email)
search.send_keys(Keys.RETURN)

# PASSWORD

try:
    search = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
    )
except:
    print("Password Locator failed")

time.sleep(2)

search.send_keys(password)
search.send_keys(Keys.RETURN)

time.sleep(2)

# Redirect to meet
driver.get("https://meet.google.com/")

try:
    search = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='i3']"))
    )
except:
    print("Password Locator failed")

search.send_keys(meeting_id)
search.send_keys(Keys.RETURN)

time.sleep(3)

# MUTE AUDIO AND VIDEO

# search = wait.until(
#     EC.presence_of_element_located(
#         (By.XPATH, "//div[@role='button']"))
# )
search = driver.find_elements_by_xpath(
    "//div[@role = 'button']")
print(len(search))

for element in search:
    element.click()
    time.sleep(3)

# /html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]
# try:
#     search = wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]"))
#     )
# except:
#     print("Join error")
# search.click()


time.sleep(5)

# //*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]

search = wait.until(
    EC.presence_of_element_located(
        (By.XPATH,
            "//*[@id='ow3']/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]")
    ))


print(search)

# try:
#     search = wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div/div[1]"))
#     )
# except:
#     print("Video Failed")

# search.click()

# time.sleep(2)

# # /html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]

# try:
#     search = wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]"))
#     )
# except:
#     print("Mute Failed")

# search.click()

# driver.close()
