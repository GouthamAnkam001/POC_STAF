Feature: ordering product in nyka
  Scenario: order dryfruits from nyka
    Given  first "open_website" and "maximize_the_window" and "click_on_sign_in" and "click_on_sign_in_with_mobile" and "give_mobile_number"
    And    second "click_verify" and "click_on_otp_field_enter_otp" and "click_on_verify"
    When   third "mouse_hover_to_category" and "mouse_hover_to_health_wellness" and "click_on_Health_foods"
    And    fourth "switch_to_child_window1" and "click_on_category" and "click_on_dry_fruits"
    When   fifth "click_on_preference" and "click_on_natural" and "click_on_item"
    And    sixth "switch_to_window2" and "give_pincode_in_textfield"
    Then   seventh "click_on_check" and "click_on_add_bag" and "click_cart_count"
    And    eighth "handle_iframe" and "click_remove_item" and "click_on_remove" and "switch_to_default"
    And    ninth "click_on_change_pincode" and "give_pincode_in_textfield2" and "click_on_check2" and "switch_to_window1"


#
# [switch_to_default]
#key=click
#locator_type=xpath
#locator=//span[@class='css-175whwo ehes2bo0']
#time=3