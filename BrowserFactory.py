from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_pref
from selenium.webdriver.firefox.options import Options as firefox_pref
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory:

    def get_browser(self, browser_name, browser_mode):
        if browser_name == 'chrome':
            chrome_options = chrome_pref()
            chrome_options.add_argument("--window-size=1280x800")
            if browser_mode == 'headless':
                chrome_options.add_argument("--headless")
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

        elif browser_name == 'firefox':
            firefox_options = firefox_pref()
            firefox_options.add_argument("--window-size=1280x800")
            if browser_mode == 'headless':
                firefox_options.add_argument("--headless")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

        else:
            raise Exception('"{}" is not a supported browser'.format(browser_name))

