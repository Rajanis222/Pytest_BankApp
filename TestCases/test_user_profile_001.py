import time
import random
import string

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Login_Page import Login_Class
from PageObjects.Signup_Page import Signup_class
from Utilities.additional_utilities import additional_utilites_class
from Utilities.readConfig_utility import ReadConfig_class
from Utilities.Logger_utility import logger_class


@pytest.mark.usefixtures("setup")
class Test_Login01:
    username=ReadConfig_class.username_data()
    password=ReadConfig_class.password_data()
    base_url=ReadConfig_class.base_url()
    login_url=ReadConfig_class.login_url()
    sign_up_url=ReadConfig_class.signup_url()
    log = logger_class.log_gen_method()



    @pytest.mark.sanity
    @pytest.mark.userprofile
    @pytest.mark.flaky
    # @pytest.mark.dependancy(name="test_bankapp_url_001")
    def test_bankapp_url_001(self):
        #driver=webdriver.Firefox()
        #driver.implicitly_wait(10)
        #driver.maximize_window()
        self.log.info("Testcase test_bankapp_url_001 is started")
        self.log.info(f"Opening the Bank Application URL")
        # self.driver=setup
        # self.driver.get("https://apps.credence.in/")
        self.driver.get(self.base_url)
        # Initialize test case
        self.log.info(f"Checking the Bank Application Title-->{self.driver.title}")
        if self.driver.title=="Bank Application":
            print("Test case passed:Bank Application URL Opened")
            self.log.info("Taking screenshot")
            # self.driver.save_screenshot(".\\Screenshots\\test_bankapp_url_001_pass.png")
            additional_utilites_class.take_screenshot(self.driver,"test_bankapp_url_001","Pass")
            allure.attach.file(".\\Screenshots\\test_bankapp_url_001_pass.png",attachment_type=allure.attachment_type.PNG)
            self.log.info("Testcase test_bankapp_url_001 is passed\n")
            assert True
        else:
            self.log.info("Taking screenshot")
            # self.driver.save_screenshot(".\\Screenshots\\test_bankapp_url_001_fail.png")
            additional_utilites_class.take_screenshot(self.driver, "test_bankapp_url_001", "Fail")
            print("Test case failed:Bank Application URL not opened")
            self.log.info("Testcase test_bankapp_url_001 is failed\n")
            assert False

    @pytest.mark.sanity
    @pytest.mark.userprofile
    # @pytest.mark.dependency(depends=["test_bankapp_url_001"])
    def test_bankapp_login_002(self):
        self.log.info("Testcase test_bankapp_login_002 is started")
        # Initialize test case
        # driver=webdriver.Firefox()
        # driver.implicitly_wait(10)
        # self.driver=setup
        # Open application
        self.log.info(f"opening the bank application url: {self.login_url}")
        # self.driver.get("https://apps.credence.in/login.html")
        self.driver.get(self.login_url)
        #Enter username and password
        lp=Login_Class(self.driver)
        self.log.info("Entering username")
        # lp.Enter_Username("Admin")
        lp.Enter_Username(self.username)
        self.log.info("Entering password")
        # lp.Enter_Password("Admin@123")
        lp.Enter_Password(self.password)
        self.log.info("Clicking the Login Button")
        # time.sleep(3) ----> replacing this hard coded value with explicit wait method defined in additional utitilities class
        additional_utilites_class.explicit_wait(self.driver,(By.XPATH, lp.click_login_button_xpath))
        lp.Click_Login_Button()
        self.log.info("Verifying page title")
        if self.driver.title=="Dashboard":
            self.log.info("Testcase test_bankapp_login_002 is pass")
            print("Test case is passed:Login Successfull")
            self.log.info("Taking screenshot")
            # self.driver.save_screenshot(".\\Screenshots\\test_bankapp_login_002_pass.png")
            additional_utilites_class.take_screenshot(self.driver,"test_bankapp_login_002", "pass" )
            self.log.info("Testcase test_bankapp_login_002 is passed")
            assert True
        else:
            self.log.info("Taking screenshot")
            additional_utilites_class.take_screenshot(self.driver, "test_bankapp_login_002", "fail")
            print("Test case failed:Login failed")
            self.log.info("Testcase test_bankapp_login_002 is failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.userprofile
    # @pytest.mark.dependency(depends=["test_bankapp_url_001"])
    def test_bankapp_signup_003(self,setup,faker):
        self.log.info("Testcase test_bankapp_signup_003 is started")
        self.driver=setup
        self.log.info(f"Opening the bank app url:{self.sign_up_url}")
        # self.driver.get("https://apps.credence.in/user.html")
        self.driver.get(self.sign_up_url)
        sp=Signup_class(self.driver)

        username=faker.name()
        print(f"Username: {username}")
        self.log.info("Entering username")
        sp.EnterUserName(username)

        self.log.info("Entering password")
        sp.EnterPassword("Admin@123")

        phone_number = faker.phone_number()
        print(f"phone_number: {faker.phone_number()}")
        print(f"Number generated by function {generate_random_phone_number()}")
        # time.sleep(10)
        additional_utilites_class.explicit_wait(driver=self.driver, element=(By.XPATH, sp.text_phone_xpath))
        self.log.info("Entering phone number")
        sp.EnterPhone(phone_number)

        email = faker.email()
        print(f"email: {email}")
        self.log.info("Entering email")
        sp.EnterEmail(email)
        # scroll
        self.log.info("Clicking on the create user button")
        sp.ClickCreateUserButton()
        # time.sleep(3)
        additional_utilites_class.explicit_wait(driver=self.driver, element=(By.XPATH, sp.success_message_xpath))
        self.log.info("Verifying if user created successfully")
        if sp.VerifySuccessMessage()=="signup passed":
            self.log.info("Test case test_bankapp_signup_003 is pass ")
            print("Test Case Passed: User Created Successfully")
            self.log.info("Taking screenshot")
            additional_utilites_class.take_screenshot(self.driver,"test_bankapp_signup_003","Pass")
            assert True
        else:
            self.log.info("Test case test_bankapp_signup_003 is failed")
            self.log.info("Taking screenshot")
            additional_utilites_class.take_screenshot(self.driver, "test_bankapp_signup_003", "Pass")
            print("Test Case Failed: User Not Created")
            assert False

def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k= 10))





"pytest -v -s --html=Report/my_report.html -n auto -p no:warnings"




