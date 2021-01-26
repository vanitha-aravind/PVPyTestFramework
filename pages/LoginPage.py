from selenium.common.exceptions import NoSuchElementException

from pages.locators import CommonLocators
from utilities.CommonHelper import CommonHelper


class LoginPage:
  def __init__(self, driver):
    self.driver = driver
    self.common_helper = CommonHelper(driver)

  def login_into_testing_club(self, email):
    self.common_helper.clear_and_set_value(CommonLocators.emailInput, email)
    self.driver.find_element(*CommonLocators.submitBtn).click()

  def login_status(self):
    try:
      self.common_helper.wait_for_displayed(CommonLocators.userNameDiv)
      return self.driver.find_element(*CommonLocators.userNameDiv).is_displayed()
    except:
      return False
