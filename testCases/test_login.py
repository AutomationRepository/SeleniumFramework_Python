import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.Regression
    def test_homePageTitle(self, setup):
        self.logger.info("****************** Test_001_Login *****************")
        self.logger.info("*************** Verifying Home Page Title *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************** Home Page title test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            assert False
            self.driver.close()
            self.logger.error("*************** Home Page title test is failed *****************")

    @pytest.mark.Regression
    def test_login(self, setup):
        self.logger.info("*************** Verifying Login test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*************** Verifying login test passed *****************")
        else:
            assert False
            self.driver.close()
            self.logger.error("*************** Verifying login test failed *****************")
