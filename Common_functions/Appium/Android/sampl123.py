from android_keyword_mapping import *
from Common_functions.Utilities.config import get_data

path = r'C:\Users\GANMAHES\PycharmProject\POC1\Test_Examples\android_test_case\features\configuration\android\contacts.ini'
android_key_word.run_keywords(keyword="click",locator_type=get_data(path,"click_to_phone_no","locator_type1"),locator=get_data(path,"click_to_phone_no","locator1"),timeout1=get_data(path,"click_to_phone_no","timeout"))
