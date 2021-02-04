import time
from pages.CalanderPage import CalanderPage


def test_Calander(driver):
    calander = CalanderPage(driver)
    calander.Calander()

