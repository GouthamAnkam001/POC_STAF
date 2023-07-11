"""
__ Author name__ = A Goutham
__email__        = gouthamankam2000@gmail.com
__Date__         = 27-1-2023
THis module is the abstracted module for implementing the selenium methods by appropriate keywords
"""
import sys
from Common_functions.selenium.web_logging_file import *
import time
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Test_Examples.web_test_case.features.Configurations.web_capabilities import capabilities
from selenium.common.exceptions import NoSuchElementException, \
    WebDriverException, \
    ElementNotInteractableException, \
    JavascriptException, \
    NoSuchWindowException, \
    NoSuchFrameException, \
    MoveTargetOutOfBoundsException
from selenium.webdriver.common.keys import Keys
from Common_functions.Check_Python import check_python_exists


class WebFunctions:
    """
    webFunctions class is a collection of selenium methods used in automation
    """

    def __init__(self):
        """
        this method creates the webdriver if python exists in the machines
        """
        if check_python_exists() and capabilities():
            check_results_exist()
            try:
                self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
                self.driver.implicitly_wait(10)
                obj_generate_logs.add_info_logs("Driver created Successfully")
            except WebDriverException as msg:
                obj_generate_logs.add_exception_logs(msg)
                self.get_screenshot()
                self.quit()
                sys.exit()
        else:
            obj_generate_logs.add_critical_logs("Mandatory Softwares are not installed! Kindly check once again")
            sys.exit()

    def navigate_to_website(self, website,timeout):
        """
        Loads a web page in the current browser session.
        :param website: the website which we want to load
        :param sec: time in seconds to wait for loading the webpage
        :return: none
        """
        try:
            self.driver.get(website)
            time.sleep(timeout)
            obj_generate_logs.add_info_logs("website is opened")
        except NoSuchWindowException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def get_element(self, locator_type, locator,timeout):

        """
        Find an element given a locator ype and locator
        webGetElement() has 3 parameters
        :param website: the website which we want to load
        :param sec: time in seconds to wait for element to be visible
        :return: none

        """
        time.sleep(timeout)
        try:
            if locator_type.upper() == "ID":
                return self.driver.find_element(By.ID, locator)
            elif locator_type.upper() == "XPATH":
                return self.driver.find_element(By.XPATH, locator)
            elif locator_type.upper() == "CSSSELECTOR":
                return self.driver.find_element(By.CSS_SELECTOR, locator)
            elif locator_type.upper() == "NAME":
                return self.driver.find_element(By.NAME, locator)
            elif locator_type.upper() == "CLASSNAME":
                return self.driver.find_element(By.CLASS_NAME, locator)
            elif locator_type.upper() == "LINK_TEXT":
                return self.driver.find_element(By.LINK_TEXT, locator)
            elif locator_type.upper() == "PARTIAL_LINK_TEXT":
                return self.driver.find_element(By.PARTIAL_LINK_TEXT, locator)
            else:
                obj_generate_logs.add_error_logs(
                    "No match of locator or locator type in predefined selenium methods for locating elements")
                self.quit()
                sys.exit()
        except NoSuchElementException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def enter_text(self, locator_type, locator, text, timeout):
        """
        webEnterText writes text to text field
        :param locator_type: takes the input of type of locator you want to find on web
        :param locator:  takes the input of locator
        :param text: text is the information you want to enter
        :param secs: time in seconds to wait for element to be visible
        :return: none
        """

        try:
            self.get_element(locator_type, locator,timeout).send_keys(text)
            time.sleep(timeout)
            obj_generate_logs.add_info_logs("Text entered")
        except ElementNotInteractableException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def click(self, locator_type, locator, timeout):
        """
        webClick() allows to click the element on web page, accepts 2 parameters
        :param locator_type: takes the input of type of locator you want to find on web
        :param locator:  takes the input of locator
        :param text: text is the information you want to enter
        :param secs: time in seconds to wait for element to be visible
        :return:none
        """
        try:
            self.get_element(locator_type, locator, timeout).click()
            time.sleep(timeout)
            obj_generate_logs.add_info_logs("clicked on element")
        except ElementNotInteractableException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def maximize_window(self,timeout):
        """
         allows to maximize the current window you are on
        :param secs: time in seconds to wait for element to be visible
        :return: none
        """
        try:
            self.driver.maximize_window()
            time.sleep(timeout)
        except WebDriverException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def quit(self):
        """
        webQuit() allows to quit the program
        """
        self.driver.quit()

    def is_displayed(self, locator_type, locator, timeout):
        """
        allows to find an element if it is displayed on web
        :param locator_type: takes the input of type of locator you want to find on web
        :param locator:  takes the input of locator
        :param text: text is the information you want to enter
        :param secs: time in seconds to wait for element to be visible
        :return: True if found else False
        """
        try:
            self.get_element(locator_type, locator, timeout).is_displayed()
            obj_generate_logs.add_info_logs("Element is displayed")
        except NoSuchElementException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def is_enabled(self, locator_type, locator, timeout):
        """
         allows to find an element if it is enabled on web
        :param locator_type: takes the input of type of locator you want to find on web
        :param locator:  takes the input of locator
        :param secs: time in seconds to wait for element to be visible
        :return: True if enabled else False
        """
        try:
            self.get_element(locator_type, locator, timeout).is_enabled()
            obj_generate_logs.add_info_logs("Element is enabled")
        except NoSuchElementException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def mouse_hover (self, locatortype, locator, timeout):
        """
        webMouseHoverOver() allows to handle MouseHoverOver actions on web
        locatortype takes the input of type of locator you want to find on web
        locatortype takes the input of locator
        """
        try:
            temp = ActionChains(self.driver)
            menu1 = self.get_element(locatortype, locator,timeout)
            temp.move_to_element(menu1).perform()
            obj_generate_logs.add_info_logs("Mouse hover over performed")
        except MoveTargetOutOfBoundsException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def get_screenshot(self):
        """
        Screenshot allows to take screenshot of the screen
        location is where you want to store the screenshot
        """
        projdir = os.getcwd()
        directory = projdir + r'\Results\web\screenshots'
        print(projdir)
        directory_is_exist = os.path.exists(directory)
        if not directory_is_exist:
            os.makedirs(directory)

        # to get file format with time stamp
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)
        file_name = str_current_datetime + ".png"

        # join filename to result\log directory
        file_path = os.path.join(directory, file_name)
        try:
            self.driver.save_screenshot(file_path)
            obj_generate_logs.add_info_logs("ScreenShot successful")
        except WebDriverException as msg:
            obj_generate_logs.add_exception_logs(msg)

    def scroll(self,timeout):
        """
        webScroll() allows to move down the scroll bar
        it by defaultly moves down by amount of 100
        """
        try:
            time.sleep(timeout)
            self.driver.execute_script("window.scrollBy(0,100)")
            obj_generate_logs.add_info_logs("scrolled the window by 100 pixels vertically:")
        except JavascriptException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()


    def click_enter(self, locatortype, locator, timeout):
        """
        webClickEnter() allows to click enter
        locatortype takes the input of type of locator you want to find on web
        locatortype takes the input of locator
        """
        try:
            self.getelement(locatortype, locator, timeout).send_keys(Keys.ENTER)
            obj_generate_logs.add_info_logs("Pressed Enter")
        except ElementNotInteractableException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def switch_window(self,window_Index,timeout):
        """
        webChildWindow() allows to go to child window, restricted to only 1 window
        """
        try:
            time.sleep(timeout)
            self.driver.switch_to.window(self.driver.window_handles[window_Index])
            obj_generate_logs.add_info_logs("Switched Window successfully")
            time.sleep(timeout)
        except NoSuchWindowException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def popup(self,choice,timeout):
        """
        webPopup() allows users to handle the pop-up boxes
        choice has 2 values. 0 for positive responses and 1 negative responses
        """
        time.sleep(timeout)
        try:
            alert = self.driver.switch_to.alert
            if choice == 0:
                alert.accept()
                obj_generate_logs.add_info_logs("positive response clicked")
            else:
                alert.dismiss()
                obj_generate_logs.add_info_logs("Negative response clicked")
        except JavascriptException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def slider(self, locatortype, locator,amount, timeout):
        """
        The methods allow to slide towards left or right
        """
        value = self.get_element(locatortype, locator, timeout)
        try:
            ActionChains(self.driver).drag_and_drop_by_offset(value, amount, 0).perform()
            obj_generate_logs.add_info_logs("sliding performed")
        except MoveTargetOutOfBoundsException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def frame(self, locatortype, locator,timeout):
        """
        allows to locate the frame and perform operations on it.
        """
        try:
            self.driver.switch_to.frame(self.get_element(locatortype, locator,timeout))
            obj_generate_logs.add_info_logs("Switched to iframe")
        except NoSuchFrameException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def switch(self,timeout):
        """
        allows to switch to parent tab from child tab
        """
        time.sleep(timeout)
        try:
            # self.driver.switch_to.default_content()
            self.driver.switch_to.parent_frame()
            time.sleep(2)
            obj_generate_logs.add_info_logs("switched from iframe")
        except NoSuchFrameException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()

    def resize(self, locatortype, locator,xoffset,yoffset,timeout):
        """
        allows to resize the web object.
        """
        value = self.get_element(locatortype, locator,timeout)
        try:
            ActionChains(self.driver).drag_and_drop_by_offset(value, xoffset, yoffset).perform()
            obj_generate_logs.add_info_logs("Resized the element")
        except MoveTargetOutOfBoundsException as msg:
            obj_generate_logs.add_exception_logs(msg)
            self.get_screenshot()
            self.quit()
            sys.exit()
