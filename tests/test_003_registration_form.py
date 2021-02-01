
from pages.RegistationFormPage import RegistationFormPage
from fixtures.TestConstrains import registration_from_data



reg_form_two_data = registration_from_data

def test_registration_form_one(driver):
  form_two = RegistationFormPage(driver)
  form_two.fill_form_two(reg_form_two_data)
  assert form_two.gender_status(reg_form_two_data) is True

