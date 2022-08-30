from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.chrome()
    elif browser == 'firefox':
        driver = webdriver.firefox()
    else:
        driver = webdriver.ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    driver = webdriver.chrome()
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'Selenium Python framework'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Neha'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

