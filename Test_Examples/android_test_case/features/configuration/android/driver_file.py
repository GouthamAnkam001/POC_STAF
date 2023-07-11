from Common_functions.Utilities.config import get_data
from appium.webdriver import webdriver
import configparser
config=configparser.ConfigParser
import sys
from selenium.common.exceptions import WebDriverException
from Common_functions.Appium.Android.android_logging_file import *

def get_driver():
    PATH = r"C:\Users\GANMAHES\PycharmProject\POC1\Test_Examples\android_test_case\features\configuration\android\properties.ini"
    # desired_capabilities = get_data(PATH, "capabilities1", "mobile")
    # str1 = str(desired_capabilities)
    # dic2 = eval(str1)
    # print(type(dic2))
    # print(dic2)
    # return dic2
    desired_capabilities = {}
    section = 'capabilities'
    for key, value in config[section].items():
        desired_capabilities[key] = value
    # self.__d_c = mobile_capabilities.capabilities()
    print(desired_capabilities)
    try:
        url = "http://127.0.0.1:4723/wd/hub"
        driver = webdriver.R(url, desired_capabilities)
        print("driver created")
    except WebDriverException as msg:
        obj_generate_logs.add_critical_logs("driver object not created")
        print(f"{msg} : unable to create driver")
        sys.exit()
