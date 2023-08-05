import streamlit as st
import Utils.CommonValidators as Validator
import Services.CustomerRecordService as CustomerRecordService
import Services.WalletTransactionService as WalletTransactionService
from datetime import datetime
import Constants

st.set_page_config(
    page_title="Offer Tacker",
    page_icon="👋",
)

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
            st.warning(f"Will take around 1 minute to reflect.")

def RenderRedeemOptions():
    inputColumn, confirmButtonColumn = st.columns([1,1])
    AmountToRedeem = 0

    with inputColumn:
        AmountToRedeem = st.sidebar.number_input("Amount to Redeem", value=0)
    with confirmButtonColumn:  
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
        st.warning(f"Will take around 1 minute to reflect.")

def SearchAndRenderCustomerOnScreen(searchQuery, newSearch = True):
    st.session_state.SearchQuery = searchQuery
    
    if newSearch:
        st.session_state.ShowRedeemOptionOnUI = False
    elif st.session_state.ShowRedeemOptionOnUI:
        RenderRedeemOptions()
        
    #Accept input and Validate it
    if searchQuery and Validator.IdentifyPhoneNumberOrEmail_AndValidate_AndThrow(searchQuery, "Customer"):

        (customer, customerRowId) = GetCachedCustomerBySearchQuery(searchQuery)
        if customer is not None:
            # st.write(customer)
            Name = st.text_input(label = "Customer name", value = customer[1])
            PhoneNumber = st.text_input(label = f"{customer[1]}'s Phone number", value = customer[4])
            Email = st.text_input(label = f"{customer[1]}'s email", value = customer[5])
            SpecialOccasion = st.date_input(label = f"{customer[1]}'s special occasion", value = datetime.strptime(customer[7], Constants.DateTimeFormat))
            # Gender = st.selectbox("Provide the Customer gender", ("Male", "Female", "Others"), value = ??)
            
            WalletColumn, RedeemButtonColumn = st.columns([1,1])
            with WalletColumn:
                st.text_input(f"{customer[1]}'s Wallet balance", value = customer[3])
            with RedeemButtonColumn:
                st.write("")
                st.write("")
                st.button(
                    label = "Redeem", 
                    disabled = customer[3] is None or float(customer[3]) <= 0, 
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

if SearchCustomerButton:
    """Triggered when search for a customer is given
    """
    SearchAndRenderCustomerOnScreen(SearchQueryInput)

elif st.session_state.SearchQuery is not None:
    SearchAndRenderCustomerOnScreen(st.session_state.SearchQuery, False)


