import configparser
from Common_functions.Appium.Android.android_keyword_mapping import *

def listing_sections(section_name):
    print("entered into andrid listing file")
    print("Section names in Listing file are :",section_name)
    config= configparser.ConfigParser()
    path= r"C:\Users\GANMAHES\PycharmProject\POC1\Test_Examples\android_test_case\features\configuration\android\contacts.ini"
    config.read(path)
    contents=dict(config[section_name])
    list1=list(contents.values())
    print("The section values in Listing file are :",list1)
    android_key_word.run_keywords(list1)

