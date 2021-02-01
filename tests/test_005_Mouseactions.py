import time

from pages.Mouseactionspage import MouseactionsPage
from selenium.webdriver.support.ui import WebDriverWait

def test_Mouseactions(driver):
    mouseaction = MouseactionsPage(driver)
    mouseaction.Hovermenu()

