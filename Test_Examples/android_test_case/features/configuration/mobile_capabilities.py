# import configparser
# import sys
#
# config = configparser.ConfigParser()
# PATH = r"C:\Users\GANMAHES\PycharmProject\POC1\Test_Examples\android_test_case\features\configuration\android\properties.ini"
# config.read(PATH)
#
# def capabilities(file, section, key):
# # def capabilities():
#     platform_name = config['capabilities']['platform_name']
#     na = {}
#     if platform_name.lower() == "android":
#         platform_version = config['capabilities']['platform_version']
#         device_name = config['capabilities']['device_name']
#         UD_ID = config['capabilities']['platform_UDID']
#         app_package = config['capabilities']['app_package']
#         app_activity = config['capabilities']['app_activity']
#         d_c = {
#             "platformName": platform_name,
#             "appium:platformVersion": platform_version,
#             "appium:deviceName": device_name,
#             "UD_ID": UD_ID,
#             "appium:appPackage": app_package,
#             "appium:appActivity": app_activity,
#             "appium:noReset": True
#         }
#         return d_c
#     else:
#         print("cannot choose other than android")
#         sys.exit()
#
#
#
from Common_functions.Utilities.config import get_data



def capabilities():
    PATH = r"C:\Users\GANMAHES\PycharmProject\POC1\Test_Examples\android_test_case\features\configuration\android\properties.ini"
    desired_capabilities = get_data(PATH,"capabilities1","mobile")
    str1= str(desired_capabilities)
    dic2 = eval(str1)
    return dic2



