from selenium import webdriver
import pytest

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':

        driver = webdriver.Chrome(options=ops)
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print('launching edge browser')
    else:
        driver = webdriver.Chrome(options=ops)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########################  pytest HTML report ########################

def pytest_configure(config):
    config._metadata['Project Name'] = 'e-bankproject'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Shridhar'
