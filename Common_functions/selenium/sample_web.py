from Common_functions.selenium.web_keyword_mapping import *
from ini import readConfig
from basic import split

path=r"C:\Users\GANMAHES\PycharmProject\POC1\test_data.ini"
web_KeywordMapping.run_keywords(split("SignIN_click_xpath"),readConfig(path,"login","email"))