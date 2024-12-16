import time

import openpyxl
import pytest
from selenium.webdriver.common.by import By

from PageObjects.Customer_Search_Page import Customer_Search_Class
from Utilities import Excel_utility


@pytest.mark.usefixtures("setup")

class Test_User_Search:
    Excel_file=".\\TestData\\Test_data.xlsx"
    driver=None

    def test_bankapp_customer_search_excel(self, bankapp_login):
        cs=Customer_Search_Class(self.driver)
        cs.Click_Customer_Management_Link()
        row_count=Excel_utility.Max_Row_Count_Excel(self.Excel_file,"Customer_Search")
        print(f"Number of rows in excel:{row_count}")
        testcase_status=[]
        for i in range(2,row_count+1):
            self.customerID=Excel_utility.Read_Data_From_Excel_File(self.Excel_file,"Customer_Search", i, 2)
            self.expected_result=Excel_utility.Read_Data_From_Excel_File(self.Excel_file,"Customer_Search", i, 3)
            print(f"customer ID:{self.customerID}")
            print(f"Expected result:{self.expected_result}")
            cs.Enter_CustomerID(self.customerID)
            search_customer_button=self.driver.find_element(By.XPATH, cs.search_customer_button_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", search_customer_button)
            cs.Click_Search_Customer_Button()
            time.sleep(3)
            if cs.Get_CustomerID_Search_Result()=="Pass" and self.expected_result=="Pass":
                print("Customer search successful")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Customer_Search", i, 4, "Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Customer_Search", i, 5, "Pass")
            elif cs.Get_CustomerID_Search_Result()== "Fail" and self.expected_result=="Fail":
                print("Customer search failed")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Customer_Search", i, 4, "Fail")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Customer_Search", i, 5, "Pass")
            else:
                print("Customer search failed")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Customer_Search", i, 4, "Fail")
                Excel_utility.Write_Data_To_Excel_File(self.Excel_file, "Customer_Search", i, 5, "Fail")
            self.driver.back()
            search_customerID_textbox=self.driver.find_element(By.XPATH,cs.text_customer_id_xpath)
            search_customerID_textbox.clear()

        print(f"testcase_status:{testcase_status}")
        if "Fail" not in testcase_status:
            print("All testcases passed")
            assert True
        else:
            print("Test case failed")
            assert False
