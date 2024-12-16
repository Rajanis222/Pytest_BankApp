
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Login_Page import Login_Class
from Utilities.Logger_utility import logger_class
from Utilities.readConfig_utility import ReadConfig_class
from Utilities.additional_utilities import additional_utilites_class


# step 1
# @pytest.fixture
# def setup():
#     driver=webdriver.Firefox()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

#step 2
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_value = request.config.getoption("--browser")
    if browser_value == "chrome":
        print("""launching chrome browser""")
        driver = webdriver.Chrome()
    elif browser_value == "firefox":
        print("""launching firefox browser""")
        driver = webdriver.Firefox()
    elif browser_value == "edge":
        print("""launching edge browser""")
        driver = webdriver.Edge()
    elif browser_value == "headless":
        print("""launching headless browser""")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    # else:
    #     print("""By default launching chrome browser""")
    #     driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)
    #Attaching driver to class
    request.cls.driver=driver
    yield driver
    driver.quit()

username = ReadConfig_class.username_data()
password = ReadConfig_class.password_data()
base_url = ReadConfig_class.base_url()
login_url = ReadConfig_class.login_url()
sign_up_url = ReadConfig_class.signup_url()
log = logger_class.log_gen_method()
@pytest.fixture
def bankapp_login(setup):
    log.info("Testcase test_bankapp_login_002 is started")
    log.info(f"opening the bank application url: {login_url}")
    driver.get(login_url)
    lp = Login_Class(driver)
    log.info("Entering the Username")
    lp.Enter_Username(username)
    log.info("Entering the Password")
    lp.Enter_Password(password)
    log.info("Clicking the Login Button")
    additional_utilites_class.explicit_wait(driver, (By.XPATH, lp.click_login_button_xpath))
    lp.Click_Login_Button()

@pytest.fixture(params=[

    ("Admin", "Pass"),
    ("Tushar", "Pass"),
    ("qwert12", "Fail"),
    ("sheetal", "Pass")
])

def get_data_for_user_search(request):
    return request.param

@pytest.fixture(params=[
    ("21","Pass"),
    ("20","Fail"),
    ("169","Pass"),
    ("22","Fail")
])

def get_data_for_customer_search(request):
    return request.param

@pytest.fixture(params=[
    ("21","Pass"),
    ("20","Fail"),
    ("91","Pass"),
    ("22","Fail")
])

def get_data_for_account_search(request):
    return request.param