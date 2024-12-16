from selenium.webdriver.common.by import By


class Account_Search_Class:
    account_management_link_xpath="//a[normalize-space()='Account Management']"
    text_accountID_xpath="//input[@id='accountId']"
    search_account_button_xpath="//button[@type='submit']"
    get_searched_accountID_xpath="//div[@class='error-message']"

    def __init__(self,driver):
        self.driver=driver

    def Click_Account_Management_Link(self):
        self.driver.find_element(By.XPATH, self.account_management_link_xpath).click()

    def Enter_AccountID(self,account_ID):
        self.driver.find_element(By.XPATH, self.text_accountID_xpath).send_keys(account_ID)

    def Click_Search_Account_Button(self):
        self.driver.find_element(By.XPATH,self.search_account_button_xpath).click()

    # def Get_Account_Search_Result(self):
    #     title=self.driver.title
    #     print(title)
    #
    #     if title=="Search Account Results":
    #         AccountID_Result=self.driver.find_element(By.XPATH,self.get_searched_accountID_xpath).text
    #         print(f"Account_ID:{AccountID_Result}")
    #         return "Fail"
    #     else:
    #         return "Pass"

    def Get_Account_Search_Result(self):
        try:
            message=self.driver.find_element(By.XPATH,self.get_searched_accountID_xpath)
            if message.is_displayed():
                print("Account not found")
            return "Fail"
        except:
            print("Account is found")
            return "Pass"


