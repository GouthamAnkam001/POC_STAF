"""
__ Author name__ = A Goutham
__email__        = gouthamankam2000@gmail.com
__Date__         = 27-1-2023
THis module helps in mapping selenium automation methods through the keywords
"""
import sys

from Common_functions.selenium.web_functions import WebFunctions


class WebKeywordMapping(WebFunctions):
    """
    # _keywordMapping class has only one method
    it takes the keyword from user and finds it's appropriate implementation in match case
    """

    def run_keywords(self,keyword="_",locator_type=None,locator=None,timeout1=None,website_name=None,choice=None,text="",
window_index=None,amount=None,xoffset=None,yoffset=None):
        """
        run_keyword() has the ability to take many parameters.
        """
        timeout=int(timeout1)
        match keyword:
            case "open website":
                super().navigate_to_website(website_name, timeout)
            case "enter text":
                super().enter_text(locator_type, locator, text, timeout)
            case "screenshot":
                super().get_screenshot()
            case "click":
                super().click(locator_type, locator, timeout)
            case "maximize":
                super().maximize_window(timeout)
            case "quit":
                super().quit()
            case "is displayed":
                super().is_displayed(locator_type, locator, timeout)
            case "is enabled":
                super().is_enabled(locator_type, locator, timeout)
            case "mouse movement":
                super().mouse_hover(locator_type, locator, timeout)
            case "scroll":
                super().scroll(timeout)
            case "press enter":
                super().click_enter(locator_type, locator,timeout)
            case "switch window":
                super().switch_window(window_index, timeout)
            case "pop up":
                super().popup(choice,timeout)
            case "sliding":
                super().slider(locator_type, locator, amount,timeout)
            case "iframe":
                super().frame(locator_type, locator,timeout)
            case "switch to default content":
                super().switch(timeout)
            case "resize":
                super().resize(locator_type, locator, xoffset, yoffset, timeout)
            case _:
                print("no particular option")
                sys.exit()


web_KeywordMapping = WebKeywordMapping()
