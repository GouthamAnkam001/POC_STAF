import configparser
import sys
import logging
config = configparser.ConfigParser()
PATH = r"C:\Users\GANMAHES\PycharmProject\POC1\Test_Examples\web_test_case\features\Configurations\web\properties.ini"
config.read(PATH)


def capabilities():
    platform_name = config['capabilities']['search_engine_name']
    if platform_name == "Chrome":
        return True
    logging.error("Wrong Search Engine Selected")
    return False
