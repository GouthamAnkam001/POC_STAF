"""
importing necessary libraries
"""
import subprocess
from Common_functions.Appium.Check_Appium import check_appium_exists
from Common_functions.Check_Python import check_python_exists
import sys
import time
from Test_Examples.android_test_case.features.configuration import mobile_capabilities
from Common_functions.Appium.Android.android_logging_file import *
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from selenium.common.exceptions import WebDriverException \
    , ElementNotInteractableException, NoSuchElementException, \
    ElementNotVisibleException, StaleElementReferenceException, \
    ScreenshotException, InvalidElementStateException, \
    InvalidCoordinatesException
class AndroidFunctions:
    """
    used to create the basic keyword functions
    """

    def __init__(self):

        if check_appium_exists() and check_python_exists():
            print("entered into android functions")
            self.appium_service = AppiumService()
            self.appium_service.start(args=["--address", "127.0.0.1", "--port", "4723",
                                            "--base-path", '/wd/hub'])
            self.__d_c = mobile_capabilities.capabilities()
            print(self.__d_c)
            check_results_exist()
            try:
                self.__url = "http://127.0.0.1:4723/wd/hub"
                self.driver = webdriver.Remote(self.__url, self.__d_c)
                print("driver created")
                self.driver.implicitly_wait(20)
            except WebDriverException as msg:
                obj_generate_logs.add_critical_logs("driver object not created")
                print(f"{msg} : unable to create driver")
                self.appium_service.stop()
                sys.exit()
        else:
            obj_generate_logs.add_critical_logs("Mandatory softwares are not installed kindly check")
            print("Kindly check the installations correctly")
            sys.exit()


    def get_allure_report(self, filepath1, filename1):
        """

        :param filepath1: filepath where the file exists
        :param filename1: filename for which we need to run allure report
        :return: run the commands
        """
        try:
            os.chdir(filepath1)
            subprocess.run("behave " + filename1)
            subprocess.run("behave -f allure_behave.formatter:AllureFormatter "
                           "-o allure_report " + filename1)
            current_dir = os.getcwd()
            print(current_dir)
            os.chdir(filepath1)
            cmd = r"allure serve reports_behave"
            subprocess.run(cmd, shell=True)
        except Exception as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.appium_service.stop()
            self.driver.quit()
            sys.exit()

    def click_on_element(self, locator_type, locator,timeout):
        """
        click: This method is used to click on an element.
        :param locator_type: type of locator
        :param locator: locator for the element
        :return: element to be performed
        """
        try:
            self.check_if_element_exists(locator_type, locator,timeout).click()
        except NoSuchElementException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.appium_service.stop()
            self.driver.quit()
            sys.exit()


    def enter_text(self, locator_type, locator, data ,timeout):
        """
        sendkeys: This method is used to enter text into an input field.
        :param locator_type: type of locator
        :param locator: locator for the element
        :param data: data to be sent for sendkeysa
        :return: element to be performed
        """
        try:
            self.check_if_element_exists(locator_type, locator ,timeout).send_keys(data)
        except ElementNotInteractableException as msg:
            print(msg)
            obj_generate_logs.add_exception_logs(msg)
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def scrolling_till_element(self, locator_type1, locator1, locator_type2, locator2,timeout):
        """
        scroll: This method is used to scroll the screen until a specific element is visible.
        :param type: locator type for a
        :param locate: locator for a
        :param type2: locator type for b
        :param locate2: locator for b
        :return: scrolling from a point to b point
        """
        a_point = self.check_if_element_exists(locator_type1, locator1,timeout)
        b_point = self.check_if_element_exists(locator_type2, locator2,timeout)
        try:
            self.driver.scroll(b_point, a_point)
        except ElementNotVisibleException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()
        except StaleElementReferenceException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def get_screenshot(self):
        """

        :param path: the path where the screenshot will be stored
        :return: element to be performed
        """
        projdir = os.getcwd()
        directory1 = projdir + r'\Results\android\screenshots'

        directory_is_exist = os.path.exists(directory1)
        if not directory_is_exist:
            os.makedirs(directory1)

        # to get file format with time stamp
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)
        file_name = str_current_datetime + ".png"


        # join filename to result\log directory
        file_path = os.path.join(directory1, file_name)


        try:
            self.driver.save_screenshot(file_path)
        except ScreenshotException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def hide_keyboard(self,timeout):
        """
        :return: hides the keyboard from the screen
        """
        time.sleep(timeout)
        try:
            self.driver.hide_keyboard()
        except WebDriverException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def clear_textfield(self, locator_type, locator,timeout):
        """

        :param locator_type: type of locator
        :param locator: locator for the element
        :return: clears the text which is already present in textfield
        """
        try:
            self.check_if_element_exists(locator_type, locator ,timeout).clear()
        except InvalidElementStateException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def get_attribute(self, locator_type, locator, attribute ,timeout):
        """
        get_attribute: This method is used to retrieve the value of a
        specific attribute of an element.
        :param locator_type: type of locator
        :param locator: locator of element
        :return: value
        """
        try:
            value = self.check_if_element_exists(locator_type, locator ,timeout).get_attribute(attribute)
            return value
        except StaleElementReferenceException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def long_press(self, locator_type, locator,timeout):
        """

        :param locator_type:type of locator
        :param locator: locator of element
        :return: element to be performed
        """
        try:
            actions = TouchAction(self.driver)
            actions.long_press(self.check_if_element_exists(locator_type, locator ,timeout))
            actions.perform()
        except ElementNotInteractableException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def is_displayed(self, locator_type, locator,timeout):
        """

        :param locator_type: type of locator
        :param locator:  locator of element
        :return: element to be performed
        """
        self.check_if_element_exists(locator_type, locator,timeout).is_displayed()

    def is_enabled(self, locator_type, locator,timeout):
        """

        :param locator_type: type of locator
        :param locator:   locator of element
        :return: element to be performed
        """
        try:
            self.check_if_element_exists(locator_type, locator,timeout).is_enabled()
        except ElementNotInteractableException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def is_selected(self, locator_type, locator,timeout):
        """

        :param locator_type: type of locator
        :param locator:  locator of element
        :return: element to be performed
        """
        try:
            self.check_if_element_exists(locator_type, locator,timeout).is_selected()
        except ElementNotInteractableException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def drag_drop(self, locator_type1, locator1, locator_type2, locator2,timeout):
        """

        :param locator_type1:type of locator
        :param locator1: locator of element
        :param locator_type2: type of locator
        :param locator2: locator of element
        :return: element to be performed
        """
        try:
            source_element = self.check_if_element_exists(locator_type1, locator1,timeout)
            destination_element = self.check_if_element_exists(locator_type2, locator2,timeout)
            action = TouchAction(self.driver)
            action.long_press(source_element).move_to(destination_element).release().perform()
        except WebDriverException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def swipe_till_coordinates(self, start_x, start_y, end_x, end_y, duration,timeout):
        """
        swipe: This method is used to perform a swipe gesture on the screen.

        param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :param duration:
        :return:
        """
        time.sleep(timeout)
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        except InvalidCoordinatesException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def lock_screen(self):
        """

        :return: lock the screen
        """
        try:
            self.driver.lock()
        except WebDriverException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def press_keycode(self, key ,timeout):
        """

        :param key:
        :return:
        """
        time.sleep(timeout)
        try:
            self.driver.press_keycode(key)
        except StaleElementReferenceException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()
        except NoSuchElementException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()
        except WebDriverException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def set_orientation(self, rotate_to,timeout):
        """
        param rotate_to: screen should rotate to [landscape, portrait]

        """
        time.sleep(timeout)
        try:
            self.driver.orientation = rotate_to
        except NoSuchElementException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def move_to(self, locator_type, locator, move_a, move_b,timeout):
        """

        :param locator type: type of locator
        :param locator:  locator
        :param move_a: move to x coordinate
        :param move_b: move to y coordinate
        :return:
        """
        try:
            element = self.check_if_element_exists(locator_type, locator,timeout)
            start_x = element.location['x']
            start_y = element.location['y']
            end_x = start_x + move_a
            end_y = start_y + move_b  # Perform the touch action to move the element
            action = TouchAction(self.driver)
            action.long_press(element).move_to(x=end_x, y=end_y).release().perform()
        except NoSuchElementException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.driver.quit()
            self.appium_service.stop()
            sys.exit()

    def check_if_element_exists(self, locator_type, locator,timeout):
        """
        :param locator_type: type of locator
        :param locator: locator foe th element
        :return: element to be performed
        """
        time.sleep(timeout)
        print("The locator of get elements are : ",locator)
        locator_type_ele = locator_type.upper()
        if locator_type_ele == "ID":
            try:
                return self.driver.find_element(AppiumBy.ID, locator)
            except NoSuchElementException as msg:
                self.get_screenshot()
                obj_generate_logs.add_exception_logs(msg)
                self.driver.quit()
                self.appium_service.stop()
                sys.exit()

        elif locator_type_ele == "XPATH":
             try:
                 return self.driver.find_element(AppiumBy.XPATH, locator)
             except NoSuchElementException as msg:
                 self.get_screenshot()
                 obj_generate_logs.add_exception_logs(msg)
                 self.driver.quit()
                 self.appium_service.stop()
                 sys.exit()

        elif locator_type_ele == "NAME":
             try:
                return self.driver.find_element(AppiumBy.NAME, locator)
             except NoSuchElementException as msg:
                 obj_generate_logs.add_exception_logs(msg)
                 self.get_screenshot()
                 self.driver.quit()
                 self.appium_service.stop()
                 sys.exit()
        elif locator_type_ele == "LINK_TEXT":
             try:
                return self.driver.find_element(AppiumBy.LINK_TEXT, locator)
             except NoSuchElementException as msg:
                 obj_generate_logs.add_exception_logs(msg)
                 self.get_screenshot()
                 self.driver.quit()
                 self.appium_service.stop()
                 sys.exit()
        elif locator_type_ele == "CSS_SELECTOR":
            try:
                return self.driver.find_element(AppiumBy.CSS_SELECTOR, locator)
            except NoSuchElementException as msg:
                obj_generate_logs.add_exception_logs(msg)
                self.get_screenshot()
                self.driver.quit()
                self.appium_service.stop()
                sys.exit()

        elif locator_type_ele == "CLASS_NAME":
            try:
                return self.driver.find_element(AppiumBy.CLASS_NAME, locator)
            except NoSuchElementException as msg:
                obj_generate_logs.add_exception_logs(msg)
                self.get_screenshot()
                self.driver.quit()
                self.appium_service.stop()
                sys.exit()

        elif locator_type_ele == "ACCESSIBILITY_ID":
            try:
                return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locator)
            except NoSuchElementException as msg:
                obj_generate_logs.add_exception_logs(msg)
                self.get_screenshot()
                self.driver.quit()
                self.appium_service.stop()
                sys.exit()

        elif locator_type_ele == "TAG_NAME":
            try:
                return self.driver.find_element(AppiumBy.TAG_NAME, locator)
            except NoSuchElementException as msg:
                obj_generate_logs.add_exception_logs(msg)
                self.get_screenshot()
                self.driver.quit()
                self.appium_service.stop()
                sys.exit()
        else:
            obj_generate_logs.add_error_logs("cannot find locator type with locator in options")
            self.appium_service.stop()
            self.driver.quit()
            sys.exit()
