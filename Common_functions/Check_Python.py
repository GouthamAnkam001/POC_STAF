import platform
# import logging
from Common_functions.Appium.Android.android_logging_file import obj_generate_logs


def check_python_exists():
    if platform.python_version().replace(".", "").isdecimal():
        return True
    obj_generate_logs.add_error_logs("Python Not installed")
    return False
