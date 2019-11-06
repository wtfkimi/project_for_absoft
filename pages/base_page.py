from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage():
    def __init__(self, browser, url): # Конструктор
        self.browser = browser
        self.url = url


    def click(self, how, what): # Клик
        try:
            self.browser.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True


    def get_text(self, how, what): #Получить текст
        try:
            x = self.browser.find_element(how, what).text
        except NoSuchElementException:
            return 'NoSuchElement'
        return x


    def refresh(self):
        self.browser.refresh()


    def open(self): #Открыть юрл
        self.browser.get(self.url)


    def send_keys(self, how, what, words): #Передать текст
        try:
            x = self.browser.find_element(how, what).send_keys('{}'.format(words))
        except NoSuchElementException:
            return False
        return x


    def implicit_wait(self):
        self.browser.implicitly_wait(4)


    def presence_of_element_located(self, how, what):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((how, what)))


