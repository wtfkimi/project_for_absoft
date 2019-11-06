from selenium.webdriver.common.by import By


class Locators:
    CREATE_USER = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/nav/a[2]/span')
    ACCEPT = (By.CSS_SELECTOR, 'a.button.success')
    EMAIL_TEXT = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/div[2]/nav/a[2]/span')
    MESSAGE = (By.CSS_SELECTOR, 'li.msg_item')
    ID_FRAME = (By.ID, 'idIframe')
    LINK_TEXT1 = (By.XPATH, '/html/body/span')
    LINK_TEXT_FULL = (By.XPATH, '/html/body')