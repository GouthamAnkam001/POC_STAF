
import logging
import os
from datetime import datetime


def check_results_exist():
    projdir = os.getcwd()
    directory = projdir + r'\Results\web\logs'
    is_exist = os.path.exists(directory)
    # if not create result\log directory
    if not is_exist:
        os.makedirs(directory)
    # to get file format with time stamp
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    str_current_datetime = str(current_datetime)
    file_name = str_current_datetime + ".txt"

    # join filename to result\log directory
    file_path = os.path.join(directory, file_name)
    logging.basicConfig(
        filename=file_path, level=10, filemode='w',
        format='%(asctime)s:%(levelno)s:%(message)s')


class generate_logs:
    @staticmethod
    def add_exception_logs(message):
        # logging method
        logging.exception(message)

    @staticmethod
    def add_info_logs(message):
        # logging method
        logging.info(message)

    @staticmethod
    def add_warning_logs(message):
        # logging method
        logging.warning(message)

    @staticmethod
    def add_debug_logs(message):
        # logging method
        logging.debug(message)

    @staticmethod
    def add_error_logs(message):
        # logging method
        logging.error(message)

    @staticmethod
    def add_critical_logs(message):
        # logging method
        logging.critical(message)


obj_generate_logs=generate_logs()
