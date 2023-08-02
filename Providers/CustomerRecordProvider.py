from Models.Customer import Customer
from google.oauth2 import service_account
import streamlit as st
from gspread_pandas import Spread, Client
import pyparsing
from pandas import DataFrame
import Constants

# Create a Google Authentication connection object
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)

client = Client(scope=scope,creds=credentials)

# spread = Spread(spreadsheetname,client = client)

sh = client.open(Constants.GoogleSheetDbName)

workSheet = sh.worksheet(Constants.CustomerSpreadSheetName)

counterMy = 0
@st.cache_data(ttl=10)
def LoadAndShowDb():
    global counterMy
    df = DataFrame(workSheet.get_all_records())
    st.write(counterMy)
    counterMy = counterMy + 1
    st.write(df)

#LoadAndShowDb()


# @st.cache_data(ttl=600)
# def Load(query):
#     rows = conn.execute(query, headers=1)
#     rows = rows.fetchall()
#     return rows

# sheet_url = st.secrets["private_gsheets_url"]
# rows = run_query(f'SELECT * FROM "{sheet_url}"')

def AddCustomerRecord(customer: Customer):
    # nextItemId = len(workSheet.col_values(1))
    workSheet.append_row([customer.Id, customer.Name, customer.Gender, customer.Wallet, customer.PhoneNumber, customer.Email, customer.RegisteredAt, customer.SpecialOccasion, customer.Referrer])
    #LoadAndShowDb()

def GetAllCustomerRecord():
    return workSheet.get_all_records()

    