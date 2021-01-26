import time

from selenium.webdriver.common.by import By

from pages.locators import RegistrationFormLocators, CommonLocators
from utilities.CommonHelper import CommonHelper


class RegistationFormPage:
  def __init__(self, driver):
    self.driver = driver
    self.common_helper = CommonHelper(driver)

  def fill_registration_common_inputs(self, form_data):
    self.driver.find_element(*RegistrationFormLocators.emailInput).send_keys(form_data.get('email'))
    self.driver.find_element(*RegistrationFormLocators.passwordInput).send_keys(form_data.get('password'))
    self.driver.find_element(*RegistrationFormLocators.cnfPasswordInput).send_keys(form_data.get('password'))
    self.driver.find_element(*RegistrationFormLocators.firstNameInput).send_keys(form_data.get('first_name'))
    self.driver.find_element(*RegistrationFormLocators.lastNameInput).send_keys(form_data.get('last_name'))
    self.driver.find_element(*RegistrationFormLocators.userNameInput).send_keys(form_data.get('username'))
    self.driver.find_element(*RegistrationFormLocators.aboutMeTextArea).send_keys(form_data.get('about_me'))

  def form_two_additional_inputs(self, form_data):
    self.driver.find_element(By.CSS_SELECTOR, f'[value*="{form_data.get("gender")}"]').click()
    for hobby in form_data.get('hobbies'):
      self.driver.find_element_by_css_selector(f'[name="{hobby}"]').click()

  def submit_registration_form(self):
    self.driver.find_element(*CommonLocators.submitBtn).click()

  def fill_form_one(self, form_data):
    self.common_helper.goto_pages('Registration Form', 'Form 1')
    self.fill_registration_common_inputs(form_data)
    self.submit_registration_form()

  def fill_form_two(self, form_data):
    self.common_helper.goto_pages('Registration Form', 'Form 2')
    self.fill_registration_common_inputs(form_data)
    self.form_two_additional_inputs(form_data)
    self.submit_registration_form()




  def gender_status(self, form_data):
    return self.driver.find_element(By.CSS_SELECTOR, f'[value*="{form_data.get("gender")}"]').is_selected()
