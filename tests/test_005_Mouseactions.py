import time

from pages.Mouseactionspage import MouseactionsPage

def test_mouseactions(driver):
    mouseaction = MouseactionsPage(driver)
    mouseaction.Hovermenu()
    mouseaction.Dragmenu()







