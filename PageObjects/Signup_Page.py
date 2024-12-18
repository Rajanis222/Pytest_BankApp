from selenium.webdriver.common.by import By


class Signup_class:
    text_username_xpath="//input[@id='username']"
    text_password_xpath="//input[@id='password']"
    text_email_xpath="//input[@id='email']"
    text_phone_xpath="//input[@id='phone']"
    click_createuser_button_xpath="//button[@id='createUserButton']"
    success_message_xpath="//div[@id='successMessage']"

    def __init__(self, driver):
        self.driver = driver

    def EnterUserName(self,name):
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(name)
    def EnterPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)
    def EnterEmail(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)
    def EnterPhone(self, phone):
        createuser_button = self.driver.find_element(By.XPATH, self.click_createuser_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", createuser_button)
        createuser_button.click()
        self.driver.find_element(By.XPATH,self.text_phone_xpath).send_keys(phone)
    def ClickCreateUserButton(self):
        createuser_button = self.driver.find_element(By.XPATH, self.click_createuser_button_xpath)
        # self.driver.execute_script("arguments[0].scrollIntoView();", createuser_button)
        createuser_button.click()

    def VerifySuccessMessage(self):
        try:
            msg=self.driver.find_element(By.XPATH,self.success_message_xpath)
            print(msg.text)
            return "signup passed"
        except:
            print(msg.text)
            return "signup failed"
