
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
import argparse
from argparse import ArgumentParser
from getpass import getpass


parser = ArgumentParser(description="arg parser hidden password input.")
parser.add_argument('-sp', '--secure_password', action='store_true', dest='password',
                    help='hidden password prompt')
parser.add_argument('-e', '--email', type=str,
                    dest='email', help='email prompt')
parser.add_argument('-id', '--meeting_id', type=str,
                    dest='id', help='meeting id prompt')
args = parser.parse_args()

if args.password:
    password = getpass()

email = args.email
MeetId = args.id


def createDriverAndWait(PATH, firefox_profile):
    driver = webdriver.Firefox(
        executable_path=PATH, firefox_profile=firefox_profile)
    wait = WebDriverWait(driver, 10)
    return driver, wait


def goToLogin(email, password, driver, wait):
    driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
    try:
        search = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='identifierId']")))
    except:
        print("Email locator failed")
    time.sleep(1)
    search.send_keys(email)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        search = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
        )
    except:
        print("Password Locator failed")
    time.sleep(1)
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(1)


def GoToMeet(driver, wait, meeting_id):
    driver.get("https://meet.google.com/")
    time.sleep(1)
    try:
        search = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='i3']"))
        )
    except:
        print("Meeting ID Locator failed")

    search.send_keys(meeting_id)
    search.send_keys(Keys.RETURN)


def MuteAudioAndVideo(driver, wait):
    # aria-label for mute audio : Turn off microphone (ctrl + d)
    # aria-label for mute video : Turn off camera (ctrl + e)
    # get an array of elements which have role button

    clickableElements = driver.find_elements_by_xpath("//div[@role='button']")
    muteAudio = clickableElements[0]
    muteVideo = clickableElements[1]
    joinButton = clickableElements[3]

    muteAudio.click()
    muteVideo.click()
    time.sleep(3)
    joinButton.click()
    time.sleep(1)


def main():
    global email, password, MeetId
    PATH = "geckodriver.exe"
    # firefox profiles
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("intl.accept_languages", "en-us")
    firefox_profile.set_preference("permissions.default.microphone", 1)
    firefox_profile.set_preference("permissions.default.camera", 1)

    driver, wait = createDriverAndWait(PATH, firefox_profile)
    goToLogin(email, password, driver, wait)
    time.sleep(2)
    GoToMeet(driver, wait, MeetId)
    time.sleep(2)
    MuteAudioAndVideo(driver, wait)


if __name__ == '__main__':
    main()

# PATH = "geckodriver.exe"

# # firefox profiles
# firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference("intl.accept_languages", "en-us")
# firefox_profile.set_preference("permissions.default.microphone", 1)
# firefox_profile.set_preference("permissions.default.camera", 1)


# # driver declaration
# driver = webdriver.Firefox(
#     executable_path=PATH, firefox_profile=firefox_profile)

# # WebDriverWait initialization
# wait = WebDriverWait(driver, 10)

# # authorization too google

# # EMAIL
# driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

# try:
#     search = wait.until(EC.presence_of_element_located(
#         (By.XPATH, "//*[@id='identifierId']")))
# except:
#     print("Email locator failed")

# email = "MYGMAIL"
# password = "MYPASSWORD"
# meeting_id = "pqc-qosw-zag"
# # mute_xpath = "//*[@id=yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span"
# # video_xpath = "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div/div[1]"

# time.sleep(2)

# search.send_keys(email)
# search.send_keys(Keys.RETURN)

# # PASSWORD

# try:
#     search = wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
#     )
# except:
#     print("Password Locator failed")

# time.sleep(2)

# search.send_keys(password)
# search.send_keys(Keys.RETURN)

# time.sleep(2)

# # Redirect to meet
# driver.get("https://meet.google.com/")

# try:
#     search = wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, "//*[@id='i3']"))
#     )
# except:
#     print("Password Locator failed")

# search.send_keys(meeting_id)
# search.send_keys(Keys.RETURN)

# time.sleep(3)

# # MUTE AUDIO AND VIDEO

# # search = wait.until(
# #     EC.presence_of_element_located(
# #         (By.XPATH, "//div[@role='button']"))
# # )
# search = driver.find_elements_by_xpath(
#     "//div[@role = 'button']")
# print(len(search))

# for element in search:
#     element.click()
#     time.sleep(3)

# # /html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]
# # try:
# #     search = wait.until(
# #         EC.presence_of_element_located(
# #             (By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]"))
# #     )
# # except:
# #     print("Join error")
# # search.click()


# time.sleep(5)

# # //*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]

# search = wait.until(
#     EC.presence_of_element_located(
#         (By.XPATH,
#             "//*[@id='ow3']/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]")
#     ))


# print(search)

# # try:
# #     search = wait.until(
# #         EC.presence_of_element_located(
# #             (By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div/div[1]"))
# #     )
# # except:
# #     print("Video Failed")

# # search.click()

# # time.sleep(2)

# # # /html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]

# # try:
# #     search = wait.until(
# #         EC.presence_of_element_located(
# #             (By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]"))
# #     )
# # except:
# #     print("Mute Failed")

# # search.click()

# # driver.close()
