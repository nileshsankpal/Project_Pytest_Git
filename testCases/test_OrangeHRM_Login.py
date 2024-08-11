import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.Login_Page import logingpage_Class
from utilities.Loggerfile import LogGenerator
from utilities.ReadConfiFile import ReadConfig_Class

class Test_OrangeHRM_login:

    Username = ReadConfig_Class.getusername()
    password = ReadConfig_Class.getpassword()
    log = LogGenerator.loggen()
    def test_orangehrm_url_001(self,setup):
        self.log.debug("this is debug")
        self.log.info("this is info")
        self.log.warning("this is warning")
        self.log.error("this is error")
        self.log.critical("this is critical")
        self.log.critical("started the test_orangehrm_url_001")

        self.driver = setup
        self.lp = logingpage_Class (self.driver)
        self.log.info("start loging")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.log.info("opening browser")
        print("driver.title" + self.driver.title)
        if self.driver.title == "OrangeHRM":
            time.sleep(2)
            self.log.info("test is pass")
            self.driver.save_screenshot(".\\Screenshorts\\test_orangehrm_url_001_pass.png")
            assert True

        else:
            time.sleep(2)
            self.log.info("test is fail")
            self.driver.save_screenshot(".\\Screenshorts\\test_orangehrm_url_001_fail.png")
            assert False
        self.log.info("test case is close")
        self.driver.quit()
        self.log.info("test case is completed")




    def test_orangehrm_url_002(self,setup):
        self.log.info("test case is started")
        self.driver = setup
        self.lp =logingpage_Class(self.driver)
        self.log.info("test case is loging ")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(4)
        print("username--" + self.Username )
        print("password--" + self.password)
        self.log.info("username--" + self.Username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_UserName(self.Username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.log.info("password--" + self.password)
        self.lp.Enter_Password(self.password)
        time.sleep(2)
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.lp.Click_LoginButton()
        self.log.info("logining stauts")


        if self.lp.Validation_login_Stauts() == "Loginpass" :
            time.sleep(2)
            self.lp.Menu_Button()
            self.log.info("menu button")
            self.lp.click_Loginout_Xpath()
            time.sleep(4)
            self.driver.save_screenshot(".\\Screenshorts\\test_orangehrm_url_002_pass.png")
            self.log.info("test case is pass")
            print("User login test case is passed")

        else:
            time.sleep(2)
            self.log.info("test case is fail")
            self.driver.save_screenshot(".\\Screenshorts\\test_orangehrm_url_002_fail.png")
            print("User login test case is failed")
            self.log.info("test case is completed")
