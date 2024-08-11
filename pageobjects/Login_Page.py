import time
from selenium.webdriver.common.by import By

class logingpage_Class:

    Text_username_Xpath = (By.XPATH, "//input[@placeholder='Username']")
    Text_password_Xpath = (By.XPATH, "//input[@placeholder='Password']")
    click_loginButtonXpath = (By.XPATH, "//button[@type='submit']")
    Menu_Xpath = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    click_Loginout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver

    def Enter_UserName(self,username):
    def Enter_UserName(self,username):
        self.driver.find_element(*logingpage_Class.Text_username_Xpath).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*logingpage_Class.Text_password_Xpath).send_keys(password)

    def Click_LoginButton(self):
        self.driver.find_element(*logingpage_Class.click_loginButtonXpath).click()

    def Menu_Button(self):
        self.driver.find_element(*logingpage_Class.Menu_Xpath).click()

    def click_Loginout(self):
       self.driver.find_element(*logingpage_Class.click_Loginout_Xpath).click()

    def Validation_login_Stauts(self):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
            print("User login test case is passed")

        except:
            print("User login test case is failed")

