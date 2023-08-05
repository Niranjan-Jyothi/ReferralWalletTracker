from Models.Customer import Customer
from Models.WalletTransaction import WalletTransaction
from google.oauth2 import service_account
import streamlit as st
from gspread_pandas import Client
from pandas import DataFrame
import Constants
import pyparsing
# from gspread_pandas import Spread

# Create a Google Authentication connection object
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)

client = Client(scope=scope,creds=credentials)

# spread = Spread(spreadsheetname,client = client)

sh = client.open(Constants.GoogleSheetDbName)

"""""""""""""""Providers for CustomerRecord sheet"""""""""""""""""""""""""""""""""""""""""""""""

workSheetCustomerRecord = sh.worksheet(Constants.CustomerSpreadSheetName)

def LoadAndShowDb():
    df = DataFrame(workSheetCustomerRecord.get_all_records())
    st.write(df)

#LoadAndShowDb()

def AddCustomerRecord(customer: Customer):
    # nextItemId = len(workSheet.col_values(1))
    workSheetCustomerRecord.append_row([customer.Id, customer.Name, customer.Gender, customer.Wallet, customer.PhoneNumber, customer.Email, customer.RegisteredAt, customer.SpecialOccasion, customer.Referrer])
    #LoadAndShowDb()

def GetAllCustomerRecord():
    return workSheetCustomerRecord.get_all_records()

#Hard matches an item on the entire sheet and returns the row in which it is found
def FindCustomerIdByItem(searchItem: str) -> int:
    cell = workSheetCustomerRecord.find(searchItem)
    return -1 if cell is None else cell.row

#Pass in the row Id, to get the respective customer details
def FindCustomerByRowId(row: int):
    if row > 1:
        return workSheetCustomerRecord.row_values(row)

def DeleteCustomerByRowId(row: int):
    if row > 2:
        workSheetCustomerRecord.delete_row(row)

def UpdateCustomerWallet(amount: int, row: int, column: int):
    if row > 1 and column == Constants.CustomerRecordColumnNumberWallet:
        workSheetCustomerRecord.update_cell(row, column, amount)




"""""""""""""""Providers for WalletCreditHistory sheet"""""""""""""""""""""""""""""""""""""""""""""""

workSheetWalletCreditHistory = sh.worksheet(Constants.WalletCreditHistorySheetName)


def AddWalletTransaction(walletRecord: WalletTransaction):
    if walletRecord.CustomerId > 0:
        workSheetWalletCreditHistory.append_row(
            [walletRecord.CustomerId, walletRecord.Amount, walletRecord.TransactionType, walletRecord.TransactedAt, walletRecord.ValidUntil, walletRecord.Comment]
        )