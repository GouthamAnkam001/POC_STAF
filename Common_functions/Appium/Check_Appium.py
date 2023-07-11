import subprocess
# import logging
from Common_functions.Appium.Android.android_logging_file import *


def check_appium_exists():
    if subprocess.check_output(['appium', '--version'], shell=True):
        return True
    obj_generate_logs.add_error_logs("Appium is not installed in the device")
    return False
