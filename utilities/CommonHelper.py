from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CommonHelper:

  def __init__(self, driver):
    self.driver = driver

  # click on the menu items in the page link and sub_link are strings [Menu Name]
  def goto_pages(self, link, sub_link=None):
    if sub_link is not None:
      try:
        self.driver.find_element(By.PARTIAL_LINK_TEXT, sub_link).click()
      except:
        self.driver.find_element(By.PARTIAL_LINK_TEXT, link).click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, sub_link).click()
    else:
      self.driver.find_element(By.PARTIAL_LINK_TEXT, link).click()

  def clear_and_set_value(self, locator, new_value):
    element = self.driver.find_element(*locator)
    element.clear()
    element.send_keys(new_value)

  # Initiating explicit wait time for the selenium webdriver
  def wait(self, delay):
    return WebDriverWait(self.driver, delay)

  # Wait for the element to display(visible=True) or disappear(visible=False)
  def wait_for_displayed(self, locator, delay=20):
    self.wait(delay).until(expected_conditions.visibility_of_element_located(locator))

  def wait_for_title(self, title, delay=20):
    self.wait(delay).until(expected_conditions.title_contains(title))
