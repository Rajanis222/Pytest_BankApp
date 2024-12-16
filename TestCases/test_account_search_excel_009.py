import time

import openpyxl
import pytest
from selenium.webdriver.common.by import By

from PageObjects.Account_Search_Page import Account_Search_Class
from Utilities import Excel_utility


@pytest.mark.usefixtures("setup")

class Test_Account_Search:
    Excel_file=".\\TestData\\Test_data.xlsx"
    driver=None

    def test_bankapp_account_search_excel(self, bankapp_login):
        acs=Account_Search_Class(self.driver)
        acs.Click_Account_Management_Link()
        row_count=Excel_utility.Max_Row_Count_Excel(self.Excel_file,"Account_Search")
        print(f"Number of rows in excel:{row_count}")
        testcase_status=[]
        for i in range(2,row_count+1):
            self.accountID=Excel_utility.Read_Data_From_Excel_File(self.Excel_file,"Account_Search", i, 2)
            self.expected_result=Excel_utility.Read_Data_From_Excel_File(self.Excel_file,"Account_Search", i, 3)
            print(f"Account ID:{self.accountID}")
            print(f"Expected result:{self.expected_result}")
            acs.Enter_AccountID(self.accountID)
            search_account_button=self.driver.find_element(By.XPATH, acs.search_account_button_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", search_account_button)
            acs.Click_Search_Account_Button()
            time.sleep(3)
            if acs.Get_Account_Search_Result()=="Pass" and self.expected_result=="Pass":
                print("Account search successful")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Account_Search", i, 4, "Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Account_Search", i, 5, "Pass")
            elif acs.Get_Account_Search_Result()== "Fail" and self.expected_result=="Fail":
                print("Account search failed")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Account_Search", i, 4, "Fail")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Account_Search", i, 5, "Pass")
            else:
                print("Account search failed")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Customer_Search", i, 4, "Fail")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Customer_Search", i, 5, "Fail")
            self.driver.back()
            search_accountID_textbox = self.driver.find_element(By.XPATH, acs.text_accountID_xpath)
            search_accountID_textbox.clear()

        print(f"testcase_status:{testcase_status}")
        if "Fail" not in testcase_status:
            print("All testcases passed")
            assert True
        else:
            print("Test case failed")
            assert False
