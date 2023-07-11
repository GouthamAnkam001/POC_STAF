from Common_functions.selenium.web_keyword_mapping import *
from Common_functions.Utilities.config import get_data

path = r'C:\Users\GANMAHES\PycharmProject\POC1\Test_Examples\web_test_case\features\Configurations\web\nyka.ini'
web_KeywordMapping.run_keywords(keyword="open website",website_name=get_data(path,"open_website","website"),timeout1=get_data(path,"open_website","timeout"))
web_KeywordMapping.run_keywords(keyword="maximize",timeout1=get_data(path,"maximize_the_window","timeout"))
web_KeywordMapping.run_keywords(keyword="click",locator_type=get_data(path,"click_on_button","locator_type"),locator=get_data(path,"click_on_button","locator"),timeout1=get_data(path,"click_on_button","timeout"))
web_KeywordMapping.run_keywords(keyword="enter text",locator_type=get_data(path,"send_to_textfield","locator_type"),locator=get_data(path,"send_to_textfield","locator"),text=get_data(path,"send_to_textfield","data"),timeout1=get_data(path,"send_to_textfield","timeout"))

