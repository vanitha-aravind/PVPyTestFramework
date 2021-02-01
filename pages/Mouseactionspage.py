import time
from selenium.webdriver import ActionChains
from pages.locators.Mouseactionslocator import *
from utilities import CommonHelper

class MouseactionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_helper = CommonHelper(driver)

    def Hovermenu(self):
        self.common_helper.goto_pages('Mouse Actions', 'Hover Menus')
        self.driver.find_element(*HoverMenu).click()
        self.driver.find_element_by_css_selector(*HorMenu).click()
        actions= ActionChains(self.driver)
        homemenu= self.driver.find_element(*HomeMenu)
        submenu3=self.driver.find_element(*SubMenu3)
        actions.move_to_element(homemenu).move_to_element(submenu3).perform()
        time.sleep(3)
        portfolio=self.driver.find_element(*Portfolio)
        submenu2=self.driver.find_element(*SubMenu2)
        subsubmenu4=self.driver.find_element(*SubSubMenu4)
        actions.move_to_element(portfolio).move_to_element(submenu2).move_to_element(subsubmenu4).perform()

    def drag_drop(self):
        self.common_helper.goto_pages('Mouse Actions', 'Drag and Drop')
        self.driver.find_element(*DragMenu).click()
        event=self.driver.find_element(*Event)
        today=self.driver.find_element(*Today)
        action= ActionChains(self.driver)
        action.drag_and_drop(event,today).perform()
        action.click_and_hold(event).move_to_element(today).release(today).perform()