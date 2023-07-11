import subprocess

import appium
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
import time
import os
import sys
d_c={
 "appium:platformName": "Android",
        "appium:platformVersion": "10",
        "appium:deviceName": "samsung",
        "udid": "1bd50b18b10c7ece",
        "appium:appPackage": "com.samsung.android.dialer",
        "appium:appActivity": "com.samsung.android.dialer.DialtactsActivity"
# "autoAcceptAlerts": 'true'
#"appium:NoReset":"true"
}
URL="http://127.0.0.1:4723/wd/hub"
log_file_path = r"C:\Users\GANMAHES\PycharmProject\POC1\appium_logs.txt"
appium_service = AppiumService()
appium_service.start(args=["--address", "127.0.0.1", "--port", "4723",
                                            "--base-path", '/wd/hub'])

# Start the Appium server with log redirection
# appium_command = f'appium --log {log_file_path} &'
# subprocess.Popen(appium_command, shell=True)
# subprocess.run(appium_command, shell=True)

driver=webdriver.Remote(URL,d_c)
logs = driver.get_log('logcat | grep "http"')

# Print the logs
for log in logs:
    print(log['message'])

time.sleep(5)
driver.find_element(AppiumBy.ID,"com.samsung.android.dialer:id/digits").click()
# # driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText").send_keys("7989693368")
# # driver.find_element(AppiumBy.ID,"com.samsung.android.dialer:id/create_contacts_button_layout").click()
# # time.sleep(3)
# # driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]").click()
# # time.sleep(3)
# # driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.GridView/android.widget.LinearLayout[1]").click()
# # time.sleep(3)
# driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").click()
#
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"text(\"First name\")").send_keys("majd")
# time.sleep(6)
# driver.find_element(AppiumBy.ID,"com.google.android.contacts:id/save_button").click()
# time.sleep(3)

# time.sleep(2)
# a=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().text("Privacy Policy")')
# time.sleep(5)
# b=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().text("2. Objective and Scope")')
# time.sleep(5)

