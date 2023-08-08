import streamlit as st
import Constants
from google.oauth2 import service_account
from gspread_pandas import Client

@st.cache_resource(show_spinner = "Connecting to Database..")
def GetDatabaseClient():
    # Create a Google Authentication connection object
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    credentials = service_account.Credentials.from_service_account_info(
                    st.secrets[Constants.Secrets_GoogleApiKey], scopes = scope)

    client = Client(scope=scope,creds=credentials)

    # spread = Spread(spreadsheetname,client = client)

    return client.open(Constants.GoogleSheetDbName)


@st.cache_resource(show_spinner = "Loading tables..")
def GetSheetHandle(sheetName: str):

    if sheetName not in [Constants.CustomerSpreadSheetName, Constants.WalletCreditHistorySheetName]:
        st.error("Invalid sheet name!")
        return None
    
    DbClient = GetDatabaseClient() #Fetch DB
    return DbClient.worksheet(sheetName) #Returns requested sheet handler