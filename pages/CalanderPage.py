
import time
from pages.locators.CalanderLocator import *


class CalanderPage:
    def __init__(self, driver):
        self.driver = driver

    def Calander(self):
        self.driver.find_element(*gadgets).click()
        self.driver.find_element(*calander).click()
        dp1=self.driver.find_element(*datepick1)
        dp1.clear()
        time.sleep(3)
        dp1.send_keys("08/11/2020")
        dp2=self.driver.find_element(*datepick2)
        dp2.click()
        self.driver.find_element(*today).click()
        return
