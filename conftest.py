import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru', help='choose your language such as eng or ru')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if (browser_name == 'chrome'):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages' : user_language})
        print('\nstart chrome browser for test..')
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print('\nstart firefox browser for test')
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should by chrome or firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()