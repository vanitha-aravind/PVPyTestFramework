from selenium.webdriver.common.by import By

HoverMenu = (By.LINK_TEXT, 'Hover Menus')
HorMenu = (By.CSS_SELECTOR, '[href="#horizontal-mane"]')
HomeMenu = (By.XPATH, '//i[@class="fa fa-home"]')
SubMenu3 = (By.XPATH, '//ul[@class="sub-menu"])[1]/li[3]/a')
Portfolio = (By.XPATH, '//i[@class="fa fa-camera"]')
SubMenu2 = (By.XPATH, '//ul[@class="sub-menu"])[2]/li[2]/a')
SubSubMenu4 = (By.XPATH, '//ul[@class="sub-menu"])[2]/li[2]/ul/li[4]/a')

DragMenu = (By.CSS_SELECTOR, '[title*="Go to Drag"]')
Event = (By.CSS_SELECTOR, '.fc-event.ui-draggable')
Today = (By.CSS_SELECTOR, '.fc-today.fc-state-highlight')
