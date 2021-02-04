from selenium.webdriver.common.by import By

MouseAction = (By.XPATH, '//i[@class="fa fa-mouse-pointer"]')
HoverMenu = (By.XPATH, '//a[@title="Go to Hover Menus"]')
HorMenu = (By.CSS_SELECTOR, '[href="#horizontal-mane"]')
HomeMenu = (By.XPATH, '//i[@class="fa fa-home"]')
SubMenu3 = (By.XPATH, '//*[@id="horizontal-mane"]/div/nav/ul/li[3]/ul/li[3]/a')
Category = (By.XPATH, '//*[@id="horizontal-mane"]/div/nav/ul/li[5]/a/i')
SubMenu2 = (By.XPATH, '//*[@id="horizontal-mane"]/div/nav/ul/li[5]/ul/li[2]/a')
SubSubMenu2 = (By.XPATH, '//*[@id="horizontal-mane"]/div/nav/ul/li[5]/ul/li[2]/ul/li[2]/a')
DragMenu = (By.CSS_SELECTOR, '[title*="Go to Drag and Drop"]')
Event = (By.CSS_SELECTOR, '.fc-event.ui-draggable')
Today = (By.CSS_SELECTOR, '.fc-today.fc-state-highlight')
