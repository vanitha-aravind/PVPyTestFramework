import os
from datetime import datetime
import pytest
from BrowserFactory import BrowserFactory
from pages.LoginPage import LoginPage
import parser


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

def pytest_addoption(parser):
  parser.addoption('--BROWSER', action='store', default='chrome')
  parser.addoption('--BROWSER_MODE', action='store', default=None)
  parser.addoption('--TEST_URL', action='store', default='http://practice.testingclub.in/')
  parser.addoption('--EMAIL', action='store', required=True)

'''
session - per suite once
module - per module once
class - per class once
method - per test cases
'''

@pytest.fixture(scope="session")
def driver(pytestconfig):
  browser_factory = BrowserFactory()
  driver = browser_factory.get_browser(pytestconfig.getoption('BROWSER'),pytestconfig.getoption('BROWSER_MODE'))
  driver.implicitly_wait(10)
  driver.get(pytestconfig.getoption('TEST_URL'))
  login = LoginPage(driver)
  login.login_into_testing_club(pytestconfig.getoption('EMAIL'))
  yield driver


# Capture screenshot when a TC is failed
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    Extends the PyTest Plugin to take and embed screenshots in html report, whenever test fails.
    :param item:
    """
    timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f"{item.name}_{timestamp}.png"
            if item.funcargs.get('driver'):
                path = os.path.join(ROOT_DIR, 'reports', 'screenshots', file_name)
                item.funcargs['driver'].get_screenshot_as_file(f'{path}')
                if file_name:
                    html = f'<div><img src="screenshots/{file_name}" alt="screenshot" ' \
                           f'style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra

