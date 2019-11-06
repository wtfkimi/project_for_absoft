from .base_page import BasePage
import smtplib
from pages.locators import Locators
import time
import random

class GetnadaPage(BasePage):
    def open_browser_and_create_usere(self):
        self.presence_of_element_located(*Locators.CREATE_USER)
        self.click(*Locators.CREATE_USER)
        self.presence_of_element_located(*Locators.ACCEPT)
        self.click(*Locators.ACCEPT)


    def send_email(self, subject, msg):
        email = self.get_text(*Locators.EMAIL_TEXT)
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login('absoft97@gmail.com', '12587963')
            message = 'Subject:{}\n\n{}'.format(subject, msg)
            server.sendmail('absoft97@gmail.com', '{}'.format(email), message)
            server.quit()
            print('Success Email sent!')
        except:
            print('Email failed to send')


    def refreshes(self):
        self.refresh()


    def click_on_message(self):
        self.presence_of_element_located(*Locators.MESSAGE)
        self.click(*Locators.MESSAGE)
        self.presence_of_element_located(*Locators.ID_FRAME)
        self.browser.switch_to.frame(self.browser.find_element_by_id('idIframe'))


    def assert_link_text_for_cats(self):
        #self.presence_of_element_located(*Locators.LINK_TEXT1)
        #message_text = self.get_text(*Locators.LINK_TEXT1)
        self.presence_of_element_located(*Locators.LINK_TEXT_FULL)
        message_link = self.get_text(*Locators.LINK_TEXT_FULL)
        assert 'dream.io' in message_link


    def assert_link_text_for_woof(self):
        self.presence_of_element_located(*Locators.LINK_TEXT_FULL)
        message_link = self.get_text(*Locators.LINK_TEXT_FULL)
        assert 'random' in message_link


    def going_to_link_from_message_and_do_screenshot(self):
        message_link = self.get_text(*Locators.LINK_TEXT_FULL)
        self.browser.get('{}'.format(message_link))
        self.browser.get_screenshot_as_file('screen{}.png'.format(random.randint(1, 20)))

    def assert_link_text_for_floof(self):
        self.presence_of_element_located(*Locators.LINK_TEXT_FULL)
        message_link = self.get_text(*Locators.LINK_TEXT_FULL)
        assert 'randomfox' in message_link
