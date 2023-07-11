from behave import *
from Test_Examples.android_test_case.features.configuration.android.android_lisiting import listing_sections


@Given(u'open dialer "{click_to_phone_no}" and "{send_phone_no}"')
def send_phone_number(context,click_to_phone_no,send_phone_no):
    listing_sections(click_to_phone_no)
    listing_sections(send_phone_no)


@Given(u'click "{click_add_contact}" and "{click_on_create_new_contact}"')
def create_contact(context,click_add_contact,click_on_create_new_contact):
    listing_sections(click_add_contact)
    listing_sections(click_on_create_new_contact)

@When(u'"{click_on_contacts_icon}" and "{click_on_firstname}" and "{enter_firstname}"')
def send_contact_name(context,click_on_contacts_icon,click_on_firstname,enter_firstname):
    listing_sections(click_on_contacts_icon)
    listing_sections(click_on_firstname)
    listing_sections(enter_firstname)

# @When(u'"{click_on_contacts_icon}" and "{enter_firstname}"')
# def send_contact_name(context,click_on_contacts_icon,enter_firstname):
#     listing_sections(click_on_contacts_icon)
#     listing_sections(enter_firstname)


@Then(u'click on "{save_contact}" to save contact')
def save_contact(context,save_contact):
    listing_sections(save_contact)

@Then(u'get "{report}" for the above scripts')
def get_reports(context,report):
    listing_sections(report)

