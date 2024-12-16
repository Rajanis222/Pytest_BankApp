import time
import pytest
from selenium.webdriver.common.by import By

from PageObjects.User_Search_Page import User_Search_Class
from Utilities import Excel_utility


@pytest.mark.usefixtures("setup")
class Test_User_Search:
    driver=None
    Excel_File= ".\\TestData\\Test_data.xlsx"

    def test_bankapp_user_search_excel(self, bankapp_login):
        us= User_Search_Class(self.driver)
        us.Click_User_Management_Link()
        row_count=Excel_utility.Max_Row_Count_Excel(self.Excel_File,"User_Search")
        print(f"Number of rows in excel:{row_count}")
        testcase_status=[]
        for i in range(2, row_count+1):
            self.username=Excel_utility.Read_Data_From_Excel_File(self.Excel_File,"User_Search",i,2)
            self.expected_result=Excel_utility.Read_Data_From_Excel_File(self.Excel_File,"User_Search",i,3)
            print(f"Username:{self.username}")
            print(f"expected result:{self.expected_result}")
            us.Enter_UserName(self.username)
            searchuser_button = self.driver.find_element(By.XPATH, us.click_search_user_button_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", searchuser_button)
            us.Click_SearchUser_Button()
            time.sleep(3)
            if us.Get_UserName_Search_Result()=="Pass" and self.expected_result=="Pass":
                print("User search successful")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_File,"User_Search",i,4,"Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_File,"User_Search",i,5,"Pass")

            elif us.Get_UserName_Search_Result()=="Fail" and self.expected_result=="Fail":
                print("User search failed")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_File, "User_Search", i, 4, "Fail")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_File, "User_Search", i, 5, "Pass")

            else:
                print("User search failed")
                testcase_status.append("Fail")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_File, "User_Search", i, 4, "Fail")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_File, "User_Search", i, 5, "Fail")
            self.driver.back()
            search_user_textbox=self.driver.find_element(By.XPATH,us.get_searched_username_xpath)
            search_user_textbox.clear()




        print(f"testcase_status:{testcase_status}")
        if "Fail" not in testcase_status:
            print("All testcases passed")
            assert True
        else:
            print("Test case failed")
            assert False





