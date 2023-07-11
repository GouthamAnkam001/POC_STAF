from behave import *
# from web_test_case.features.Configurations.web.web_listing import web_listing_sections
from Test_Examples.web_test_case.features.Configurations.web.web_listing import web_listing_sections

@Given(u'first "{open_website}" and "{maximize_the_window}" and "{click_on_sign_in}" and "{click_on_sign_in_with_mobile}" and "{give_mobile_number}"')
def send_phone_number(context,open_website,maximize_the_window,click_on_sign_in, click_on_sign_in_with_mobile, give_mobile_number):
    web_listing_sections(open_website)
    web_listing_sections(maximize_the_window)
    web_listing_sections(click_on_sign_in)
    web_listing_sections(click_on_sign_in_with_mobile)
    web_listing_sections(give_mobile_number)

@Given(u'second "{click_verify}" and "{click_on_otp_field_enter_otp}" and "{click_on_verify}"')
def verify_with_otp(context,click_verify,click_on_otp_field_enter_otp,click_on_verify):
    web_listing_sections(click_verify)
    web_listing_sections(click_on_otp_field_enter_otp)
    web_listing_sections(click_on_verify)

@When(u'third "{mouse_hover_to_category}" and "{mouse_hover_to_health_wellness}" and "{click_on_Health_foods}"')
def selecting_item(context,mouse_hover_to_category,mouse_hover_to_health_wellness,click_on_Health_foods):
    web_listing_sections(mouse_hover_to_category)
    web_listing_sections(mouse_hover_to_health_wellness)
    web_listing_sections(click_on_Health_foods)

@When(u'fourth "{switch_to_child_window1}" and "{click_on_category}" and "{click_on_dry_fruits}"')
def choosing_item(context,switch_to_child_window1,click_on_category,click_on_dry_fruits):
    web_listing_sections(switch_to_child_window1)
    web_listing_sections(click_on_category)
    web_listing_sections(click_on_dry_fruits)

@When(u'fifth "{click_on_preference}" and "{click_on_natural}" and "{click_on_item}"')
def choosing_Preference(context,click_on_preference,click_on_natural,click_on_item):
    web_listing_sections(click_on_preference)
    web_listing_sections(click_on_natural)
    web_listing_sections(click_on_item)

@when(u'sixth "{switch_to_window2}" and "{give_pincode_in_textfield}"')
def checking_pincode(context,switch_to_window2,give_pincode_in_textfield):
    web_listing_sections(switch_to_window2)
    web_listing_sections(give_pincode_in_textfield)


@Then(u'seventh "{click_on_check}" and "{click_on_add_bag}" and "{click_cart_count}"')
def add_to_cart(context,click_on_check,click_on_add_bag,click_cart_count):
    web_listing_sections(click_on_check)
    web_listing_sections(click_on_add_bag)
    web_listing_sections(click_cart_count)

@Then(u'eighth "{handle_iframe}" and "{click_remove_item}" and "{click_on_remove}" and "{switch_to_default}"')
def remove_item(context,handle_iframe,click_remove_item,click_on_remove,switch_to_default):
    web_listing_sections(handle_iframe)
    web_listing_sections(click_remove_item)
    web_listing_sections(click_on_remove)
    web_listing_sections(switch_to_default)

@Then(u'ninth "{click_on_change_pincode}" and "{give_pincode_in_textfield2}" and "{click_on_check2}" and "{switch_to_window1}"')
def change_pincode(context,click_on_change_pincode,give_pincode_in_textfield2,click_on_check2,switch_to_window1):
    web_listing_sections(click_on_change_pincode)
    web_listing_sections(give_pincode_in_textfield2)
    web_listing_sections(click_on_check2)
    web_listing_sections(switch_to_window1)