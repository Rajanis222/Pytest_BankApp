import time
import pytest
from selenium.webdriver.common.by import By

from PageObjects.Account_Search_Page import Account_Search_Class


@pytest.mark.usefixtures("setup")
class Test_Customer_Search:
    driver = None
    def test_bankapp_customer_search_params(self, bankapp_login, get_data_for_account_search):
        accountID=get_data_for_account_search[0]
        print(f"account ID:{accountID}")
        expected_result=get_data_for_account_search[1]
        print(f"expected result:{expected_result}")
        acs=Account_Search_Class(self.driver)
        acs.Click_Account_Management_Link()
        acs.Enter_AccountID(accountID)
        search_account_button = self.driver.find_element(By.XPATH, acs.search_account_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", search_account_button)
        acs.Click_Search_Account_Button()
        time.sleep(3)
        print(f"Get_AccountID_Search_Result()--> {acs.Get_Account_Search_Result()}")
        if acs.Get_Account_Search_Result() == "Pass" and expected_result == "Pass":
            print("Account Search Successful")
            assert True
        elif acs.Get_Account_Search_Result() == "Fail" and expected_result == "Fail":
            print("Account Search failed")
            assert True
        else:
            print("Account Search Failed")
            assert False