import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help='Choose language: "ru","en", etc...')


@pytest.fixture(scope="function") #@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if user_language == None:
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome()
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox()
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    elif browser_name == None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        if user_language != None and browser_name == "chrome":
            print(f"\nstart chrome browser for test in {user_language}..")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options)
        elif user_language != None and browser_name == "firefox":
            print(f"\nstart firefox browser for test in {user_language}..")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", user_language)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox and --language not empty")
    yield browser
    print("\nquit browser..")
    browser.quit()
