from pages.locators.Gadgetsalertlocator import *


class AlertsPage:
  def __init__(self, driver):
    self.driver = driver

  def goto_alerts(self):
    # Go to Alerts Page
    self.driver.find_element(*gadgetsMenu).click()
    self.driver.find_element(*alertsMenu).click()

  def simple_alert(self):
    self.driver.find_element(*simpleAlert).click()
    self.driver.find_element(*alertOneBtn).click()
    alertText = self.driver.switch_to.alert.text
    self.driver.switch_to.alert.accept()
    return alertText
