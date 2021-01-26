
from selenium.webdriver.common.by import By

# links
reg_form_link = (By.CSS_SELECTOR, '.fa-window-restore');
reg_form_one_link = (By.CSS_SELECTOR, '[title="Go to Form 1"]')
reg_form_two_link = (By.CSS_SELECTOR, '[title="Go to Form 2"]')

# Form one ields
emailInput = (By.CSS_SELECTOR,'#email')
passwordInput = (By.CSS_SELECTOR, '[name="password"]')
cnfPasswordInput = (By.CSS_SELECTOR, '[name="cnfpassword"]')
firstNameInput = (By.CSS_SELECTOR, '[name="first_name"]')
lastNameInput = (By.CSS_SELECTOR, '[name="last_name"]')
userNameInput = (By.CSS_SELECTOR, '.username')
aboutMeTextArea = (By.CSS_SELECTOR, '#textarea')
