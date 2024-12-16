from selenium.webdriver.common.by import By


class User_Search_Class:
    click_user_management_link_xpath="//a[normalize-space()='User Management']"
    text_username_xpath="//input[@id='username']"
    click_search_user_button_xpath="//button[@type='submit']"
    get_searched_username_xpath = "//input[@id='username']"

    def __init__(self, driver):
        self.driver=driver

    def Click_User_Management_Link(self):
        self.driver.find_element(By.XPATH,self.click_user_management_link_xpath).click()

    def Enter_UserName(self,name):
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(name)

    def Click_SearchUser_Button(self):
        self.driver.find_element(By.XPATH, self.click_search_user_button_xpath).click()

    def Get_UserName_Search_Result(self):
        title=self.driver.title
        print(title)
        if title=="Edit User":
            username_result=self.driver.find_element(By.XPATH,self.get_searched_username_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", username_result)
            print(f"username_result-->: {username_result.get_attribute('value')}")
            return "Pass"
        else:
            return "Fail"