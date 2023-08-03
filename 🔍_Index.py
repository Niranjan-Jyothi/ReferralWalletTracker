import streamlit as st
import Utils.CommonValidators as Validator
import Services.CustomerRecordService as CustomerRecordService
from datetime import datetime
import Constants

st.set_page_config(
    page_title="Offer Tacker",
    page_icon="👋",
)

st.title("Search Customer")

customerRowId = 0
customer = None


def DeleteCustomer():
    if customer is not None and customerRowId > 0:
        CustomerRecordService.DeleteCustomerByRowId(customerRowId)

searchQuery = st.text_input("Enter Customer PhoneNumber/Email")

#Accept input and Validate it
if searchQuery and Validator.IdentifyPhoneNumberOrEmail_AndValidate_AndThrow(searchQuery, "Customer"):
    
    (customer, customerRowId) = CustomerRecordService.FindCustomerAndRowId_ByItem(searchQuery)
    if customer is not None:
        # st.write(customer)

        with st.form(key = "CustomerUpdateForm"):
            Name = st.text_input(label = "Customer name", value = customer[1])
            PhoneNumber = st.text_input(label = f"{customer[1]}'s Phone number", value = customer[4])
            Email = st.text_input(label = f"{customer[1]}'s email", value = customer[5])
            SpecialOccasion = st.date_input(label = f"{customer[1]}'s special occasion", value = datetime.strptime(customer[7], Constants.DateTimeFormat))
            # Gender = st.selectbox("Provide the Customer gender", ("Male", "Female", "Others"), value = ??)
            Wallet = st.text_input(f"{customer[1]}'s Wallet balance", value = customer[3])
            Update = st.form_submit_button(label = "Update Customer Record", disabled = True)
            Delete = st.form_submit_button(label = "Delete ?", on_click = DeleteCustomer)
            # Referrer = st.text_input(label = f"{customer[1]}'s Referrer registered Email OR Phone Number", value = customer[])
    
    else:
        st.error("Customer does not exist")
