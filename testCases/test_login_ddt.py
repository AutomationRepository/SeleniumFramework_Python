import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.Regression
    def test_login_ddt(self, setup):
        self.logger.info("*************** Test_002_DDT_Login *****************")
        self.logger.info("*************** Data Driven TC *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.user)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            self.driver.close()
            if actual_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("*************** Passed *****************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*************** Failed *****************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif actual_title != "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("*************** Failed *****************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*************** Passed *****************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("****** Login DDT test Passed *******")
            self.driver.close
            assert True
        else:
            self.logger.info("****** Login DDT test Failed *******")
            self.driver.close
            assert False
