import time
import pytest
from selenium.webdriver.common.by import By

from PageObjects.Customer_Search_Page import Customer_Search_Class


@pytest.mark.usefixtures("setup")
class Test_Customer_Search:
    driver = None
    def test_bankapp_customer_search_params(self, bankapp_login, get_data_for_customer_search):
        customerID=get_data_for_customer_search[0]
        print(f"username:{customerID}")
        expected_result=get_data_for_customer_search[1]
        print(f"expected result:{expected_result}")
        cs=Customer_Search_Class(self.driver)
        cs.Click_Customer_Management_Link()
        cs.Enter_CustomerID(customerID)
        search_user_button = self.driver.find_element(By.XPATH, cs.search_customer_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", search_user_button)
        cs.Click_Search_Customer_Button()
        time.sleep(3)
        print(f"Get_CustomerID_Search_Result()--> {cs.Get_CustomerID_Search_Result()}")
        if cs.Get_CustomerID_Search_Result() == "Pass" and expected_result == "Pass":
            print("Customer Search Successful")
            assert True
        elif cs.Get_CustomerID_Search_Result() == "Fail" and expected_result == "Fail":
            print("Customer Search failed")
            assert True
        else:
            print("User Search Failed")
            assert False