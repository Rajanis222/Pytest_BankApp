import pytest
from selenium.webdriver.common.by import By

from PageObjects.Account_Search_Page import Account_Search_Class


@pytest.mark.usefixtures("setup")
class Test_Account_Search:
    driver=None

    def test_bankapp_account_search(self,bankapp_login):
        acs = Account_Search_Class(self.driver)
        acs.Click_Account_Management_Link()
        acs.Enter_AccountID(21)
        search_account_button=self.driver.find_element(By.XPATH, acs.search_account_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",search_account_button)
        acs.Click_Search_Account_Button()

        if acs.Get_Account_Search_Result()=="Pass":
            print("Account search is passed")
            assert True
        else:
            print("Account search is failed")
            assert False



