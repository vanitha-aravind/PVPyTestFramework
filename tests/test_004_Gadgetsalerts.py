from pages.Gadgetalertpage import AlertsPage
from utilities.Gadgetalertassert import simpleAlertText

def test_simple_alert(driver):
 alerts = AlertsPage(driver)
 alerts.goto_alerts()
 assert alerts.simple_alert() == simpleAlertText
