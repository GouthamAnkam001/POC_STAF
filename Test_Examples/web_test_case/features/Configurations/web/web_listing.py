
import configparser
from Common_functions.selenium.web_keyword_mapping import *

def web_listing_sections(section_name):
    print("Section names in Listing file are :",section_name)
    config= configparser.ConfigParser()
    path= r"C:\Users\GANMAHES\PycharmProject\POC1\Test_Examples\web_test_case\features\Configurations\web\nyka.ini"
    config.read(path)
    contents=dict(config[section_name])
    list1=list(contents.values())
    print("The section values in Listing file are :",list1)

    web_KeywordMapping.run_keywords(list1)