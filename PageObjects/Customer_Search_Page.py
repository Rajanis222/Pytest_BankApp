from selenium.webdriver.common.by import By


class Customer_Search_Class:
    click_customer_management_link_xpath="//a[normalize-space()='Customer Management']"
    text_customer_id_xpath="//input[@id='customerId']"
    search_customer_button_xpath="//button[@type='submit']"
    get_searched_customer_userid_xpath="//input[@id='userId']"

    def __init__(self, driver):
        self.driver=driver

    def Click_Customer_Management_Link(self):
        self.driver.find_element(By.XPATH, self.click_customer_management_link_xpath).click()

    def Enter_CustomerID(self,customerID):
        self.driver.find_element(By.XPATH,self.text_customer_id_xpath).send_keys(customerID)

    def Click_Search_Customer_Button(self):
        self.driver.find_element(By.XPATH,self.search_customer_button_xpath).click()

    def Get_CustomerID_Search_Result(self):
        title=self.driver.title
        print(title)
        if self.driver.title=="Edit Customer":
            customerID_result=self.driver.find_element(By.XPATH,self.get_searched_customer_userid_xpath)
            print(f"User ID:{customerID_result.get_attribute('value')}")
            return "Pass"
        else:
            return "Fail"



