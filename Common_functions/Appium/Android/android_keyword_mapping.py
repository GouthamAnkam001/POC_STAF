"""
this file contains the class keyword_mapping
"""
from Common_functions.Appium.Android.android_functions import AndroidFunctions


class KeywordMapping(AndroidFunctions):
    """
    this class is used to map the keywords
    """

    def run_keywords(self,keyword="_",locator_type=None,locator=None,timeout1=None,move_x=None,move_y=None,data="",
attribute=None,start_x=None,start_y=None,end_x=None,end_y=None,press_key=None,rotate_to="landscape",locator1=None,
locator2=None,locator_type1=None,locator_type2=None,duration=None):
        timeout=int(timeout1)
        match keyword:
            # case "behave":
            #     super().get_allure_report(filepath1, filename1)

            case "click":
                super().click_on_element(locator_type, locator,timeout)

            case "enter_text":
                super().enter_text(locator_type, locator, data,timeout)

            case "scroll":

                super().scrolling_till_element(locator_type1, locator1, locator_type2, locator2 ,timeout)

            case "screenshot":
                super().get_screenshot()

            case "hide_keyboard":
                super().hide_keyboard(timeout)

            case "remove_text":
                super().clear_textfield(locator_type1, locator1 ,timeout)

            case "get_attribute":
                super().get_attribute(locator_type1, locator1, attribute ,timeout)

            case "is_displayed":
                super().is_displayed(locator_type1, locator1 ,timeout)

            case "is_enabled":
                super().is_enabled(locator_type1, locator1,timeout)

            case "is_selected":
                super().is_selected(locator_type1, locator1,timeout)

            case "swipe":
                super().swipe_till_coordinates(start_x, start_y, end_x, end_y, duration,timeout)

            case "lock":
                super().lock_screen()

            case "press_keycode":
                super().press_keycode(press_key,timeout)

            case "long_press":
                super().long_press(locator_type1, locator1,timeout)

            case "rotate_screen":
                super().set_orientation(rotate_to,timeout)

            case "move":
                super().move_to(locator_type1, locator1, move_x, move_y,timeout)

            case "drag_drop":
                super().drag_drop(locator_type1, locator1, locator_type2, locator2,timeout)


android_key_word = KeywordMapping()
