import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_0ptions = webdriver.ChromeOptions()
chrome_0ptions.add_argument('headless')


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("start with chrome")
        driver = webdriver.Chrome()
    elif browser == "edge":
        print("start with edge")
        driver = webdriver.Edge()
    elif browser == "firefox":
        print("start with firefox")
        driver = webdriver.Firefox()
    else:
        driver =webdriver.Chrome(options=chrome_0ptions)
        driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()
    return driver
