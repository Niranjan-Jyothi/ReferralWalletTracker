from Models.Customer import Customer
import streamlit as st
from pandas import DataFrame
import Constants
import pyparsing
from Providers.DataBaseConnection import GetSheetHandle
# from gspread_pandas import Spread


customerRecordSheetHandler = GetSheetHandle(Constants.CustomerSpreadSheetName)

def LoadAndShowDb():
    df = DataFrame(customerRecordSheetHandler.get_all_records())
    st.write(df)

#LoadAndShowDb()

def AddCustomerRecord(customer: Customer):
    # nextItemId = len(workSheet.col_values(1))
    customerRecordSheetHandler.append_row([customer.Id, customer.Name, customer.Gender, customer.Wallet, customer.PhoneNumber, customer.Email, customer.RegisteredAt, customer.SpecialOccasion, customer.Referrer])
    #LoadAndShowDb()

def GetAllCustomerRecord():
    return customerRecordSheetHandler.get_all_records()

#Hard matches an item on the entire sheet and returns the row in which it is found
def FindCustomerIdByItem(searchItem: str) -> int:
    cell = customerRecordSheetHandler.find(searchItem)
    return -1 if cell is None else cell.row

#Pass in the row Id, to get the respective customer details
def FindCustomerByRowId(row: int):
    if row > 1:
        return customerRecordSheetHandler.row_values(row)

def DeleteCustomerByRowId(row: int):
    if row > 2:
        customerRecordSheetHandler.delete_row(row)

def UpdateCustomerWallet(amount: int, row: int, column: int):
    if row > 1 and column == Constants.CustomerRecordColumnNumberWallet:
        customerRecordSheetHandler.update_cell(row, column, amount)