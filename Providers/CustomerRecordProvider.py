from Models.Customer import Customer
import Constants
from Providers.DataBaseConnection import GetSheetHandle
# from gspread_pandas import Spread


customerRecordSheetHandler = GetSheetHandle(Constants.CustomerSpreadSheetName)

def AddCustomerRecord(customer: Customer):
    customerRecordSheetHandler.append_row([customer.Id, customer.Name, customer.Gender, customer.Wallet, customer.PhoneNumber, customer.Email, customer.RegisteredAt, customer.SpecialOccasion, customer.Referrer])

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