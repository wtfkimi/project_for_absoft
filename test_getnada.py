from pages.getnada_page import GetnadaPage
from link_for_request import LinksRequest


subjects = 'Something'


message_cats = LinksRequest.CAT
woof_message = LinksRequest.WOOF
floof_image = LinksRequest.FLOOF_IMG
floof_link = LinksRequest.FLOOF_LINK


link = 'https://getnada.com/#'

def test_getnada_link_cat(browser):
    '''This is test for link cat'''
    page = GetnadaPage(browser, link)
    page.open()
    page.open_browser_and_create_usere()
    page.send_email(subject=subjects, msg=message_cats)
    page.refresh()
    page.refresh()
    page.click_on_message()
    page.assert_link_text_for_cats()
    page.going_to_link_from_message_and_do_screenshot()


def test_getnada_link_woof(browser):
    '''This is test for link woof'''
    page = GetnadaPage(browser, link)
    page.open()
    page.open_browser_and_create_usere()
    page.send_email(subject=subjects, msg=woof_message)
    page.refresh()
    page.refresh()
    page.click_on_message()
    page.assert_link_text_for_woof()
    page.going_to_link_from_message_and_do_screenshot()

def test_getnada_link_floof(browser):
    '''This is test for link floof'''
    page = GetnadaPage(browser, link)
    page.open()
    page.open_browser_and_create_usere()
    page.send_email(subject=subjects, msg=floof_link)
    page.refresh()
    page.refresh()
    page.click_on_message()
    page.assert_link_text_for_floof()
    page.going_to_link_from_message_and_do_screenshot()

def test_getnada_image_floof(browser):
    '''This is test for image_floow'''
    page = GetnadaPage(browser, link)
    page.open()
    page.open_browser_and_create_usere()
    page.send_email(subject=subjects, msg=floof_image)
    page.refresh()
    page.refresh()
    page.click_on_message()
    page.assert_link_text_for_floof()
    page.going_to_link_from_message_and_do_screenshot()