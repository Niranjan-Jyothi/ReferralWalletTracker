import streamlit as st

st.set_page_config(
    page_title="Pink Passion",
    page_icon="👋",
)

import Utils.CommonValidators as Validator
import Services.CustomerRecordService as CustomerRecordService
import Services.WalletTransactionService as WalletTransactionService
from datetime import datetime
import Constants

st.title("Search Customer")


def RedeemAmount(amountToRedeem):
    if amountToRedeem <= 0:
        st.sidebar.error("Please enter a valid amount to redeem")

    else:    
        (customer, customerRowId) = GetCachedCustomerBySearchQuery(st.session_state['SearchQuery'])
        customerCurrentWallet = float(customer[3])
        customerId = int(customer[0])
        newBalance = int((float)(customerCurrentWallet - amountToRedeem))
        
        if newBalance < 0:
            st.sidebar.error("Insufficient wallet balance")
        
        else:
            CustomerRecordService.UpdateCustomerWallet(newBalance, customerRowId)
            WalletTransactionService.AddWalletDebitRecord(amountToRedeem, customerId)
            st.sidebar.success("Amount debited.")
            GetCachedCustomerBySearchQuery.clear() #Only clearing the get customer by search query cache

def RenderRedeemOptionsOnUI():
    AmountToRedeem = 0
    (customer, _) = GetCachedCustomerBySearchQuery(st.session_state['SearchQuery'])

    AmountToRedeem = st.sidebar.number_input("Amount to Redeem", value = float(customer[3]))
    #Disable the Number input "+" and "-" steppers from UI given by default from streamlit.
    st.markdown("""
                <style>
                    button.step-up {display: none;}
                    button.step-down {display: none;}
                    div[data-baseweb] {border-radius: 4px;}
                </style>""",
                unsafe_allow_html=True)

    st.sidebar.button("Redeem Now", on_click = RedeemAmount, args = (AmountToRedeem, ))

def ShowRedeemOptions():
    st.session_state.ShowRedeemOptionOnUI = True
    


if 'ShowRedeemOptionOnUI' not in st.session_state:
    st.session_state.ShowRedeemOptionOnUI = False

if 'SearchQuery' not in st.session_state:
    st.session_state.SearchQuery = None


@st.cache_data(ttl=60, max_entries=2, show_spinner= "Finding Customer..")
def GetCachedCustomerBySearchQuery(searchQueryCached):
    return CustomerRecordService.FindCustomerAndRowId_ByItem(searchQueryCached)


def DeleteCustomer(customerRowId, customerName):
    """Delete a customer

    Args:
        customerRowId (int): Customer Row Id in the database
        customerName (_type_): Customer name to be displayed in event logs
    """
    if customerRowId > 2: #Prevent admin and header deletion
        CustomerRecordService.DeleteCustomerByRowId(customerRowId)
        SearchAndRenderCustomerOnScreen("")
        st.toast(f"Customer {customerName} deleted")
        st.cache_data.clear() #Deleting entire cache as total list of customers may be cached in some other page, and a delete of customer has to be reflected there as well.

def SearchAndRenderCustomerOnScreen(searchQuery, newSearch = True):
    st.session_state.SearchQuery = searchQuery
    
    #New search request given - Clear redeem options
    if newSearch:
        st.session_state.ShowRedeemOptionOnUI = False

    #When the function is invoked by streamlit auto refresh, we render redeem options if it was enabled in first place
    elif st.session_state.ShowRedeemOptionOnUI:
        RenderRedeemOptionsOnUI()
        
    #Accept input and Validate it
    if searchQuery and Validator.IdentifyPhoneNumberOrEmail_AndValidate_AndThrow(searchQuery, "Customer"):

        (customer, customerRowId) = GetCachedCustomerBySearchQuery(searchQuery)
        
        if customer is not None:
            # st.write(customer)
            st.text_input(label = "Customer name", value = customer[1], disabled=True)
            st.text_input(label = f"{customer[1]}'s Phone number", value = customer[4], disabled=True)
            st.text_input(label = f"{customer[1]}'s email", value = customer[5], disabled=True)
            st.date_input(label = f"{customer[1]}'s special occasion", value = datetime.strptime(customer[7], Constants.DateTimeFormat), disabled=True)
            # Gender = st.selectbox("Provide the Customer gender", ("Male", "Female", "Others"), value = ??)
            
            #To display Wallet and Redeem button side-to-side
            WalletColumn, RedeemButtonColumn = st.columns([1,1])
            
            with WalletColumn:
                st.text_input(f"{customer[1]}'s Wallet balance", value = customer[3], disabled=True)

            with RedeemButtonColumn:
                st.write("")
                st.write("")
                st.button(
                    label = "Redeem", 
                    disabled = customer[3] is None or float(customer[3]) <= 0, #Disable Redeem button if Wallet balance is Zero
                    on_click = ShowRedeemOptions)
            
            st.button(label = "Update Customer Record", disabled = True)
            st.button(label = "Delete ?", on_click = DeleteCustomer, args=(customerRowId, customer[1]))
            # Referrer = st.text_input(label = f"{customer[1]}'s Referrer Id", value = customer[])
        
        else:
            st.error("Customer does not exist")


#Form to Search customer
with st.form(key = "SearchCustomerForm", clear_on_submit = True):
    SearchQueryInput = st.text_input("Enter Customer PhoneNumber/Email")
    SearchCustomerButton = st.form_submit_button("Search 🔍")

#New Search request given 
if SearchCustomerButton:
    SearchAndRenderCustomerOnScreen(SearchQueryInput)

#Condition when page auto refreshes due to widget interaction
elif st.session_state.SearchQuery is not None:
    SearchAndRenderCustomerOnScreen(st.session_state.SearchQuery, False)


