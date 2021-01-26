from pages.LoginPage import LoginPage


def test_login_status(driver):
  login = LoginPage(driver)
  assert login.login_status()
