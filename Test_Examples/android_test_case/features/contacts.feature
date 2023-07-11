Feature: saving a number in contacts
  Scenario: save a contact
    Given  open dialer "click_to_phone_no" and "send_phone_no"
    And    click "click_add_contact" and "click_on_create_new_contact"
    When   "click_on_contacts_icon" and "click_on_firstname" and "enter_firstname"
#    When   "click_on_contacts_icon" and "enter_firstname"
    Then   click on "save_contact" to save contact
#    Then   get "report" for the above scripts
