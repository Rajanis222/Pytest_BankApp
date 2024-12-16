import pytest
from selenium.webdriver.common.by import By

from PageObjects.Customer_Search_Page import Customer_Search_Class


@pytest.mark.usefixtures("setup")
class Test_Customer_Search:
    driver=None

    def test_bankapp_customer_search(self,bankapp_login):
        cs=Customer_Search_Class(self.driver)
        cs.Click_Customer_Management_Link()
        cs.Enter_CustomerID("21")
        search_customer_button=self.driver.find_element(By.XPATH,cs.search_customer_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",search_customer_button)
        cs.Click_Search_Customer_Button()
        if cs.Get_CustomerID_Search_Result()=="Pass":
            print("Customer search passed")
            assert True
        else:
            print("Customer search failed")
            assert False