import time
import pytest
from selenium.webdriver.common.by import By

from PageObjects.User_Search_Page import User_Search_Class


@pytest.mark.usefixtures("setup")
class Test_User_Search:
    driver=None

    def test_bankapp_user_search(self,bankapp_login):
        # Instead of writing login methods again we have craeted login fixture
        us = User_Search_Class(self.driver)
        us.Click_User_Management_Link()
        us.Enter_UserName("Admin")
        searchuser_button = self.driver.find_element(By.XPATH, us.click_search_user_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", searchuser_button)
        us.Click_SearchUser_Button()
        # time.sleep(3)
        if us.Get_UserName_Search_Result()=="Pass":
            print("User search passed")
            assert True
        else:
            print("User search fail")
            assert False



