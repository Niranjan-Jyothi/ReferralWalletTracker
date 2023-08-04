import streamlit as st
import Constants
from Models.Customer import Customer as Customer
from datetime import datetime
from Utils.CommonValidators import *
from Services import CustomerRecordService, WalletCreditHistory

st.title("Register new Customer!")


def ValidateCustomerFormData() -> bool:
    errors = 0

    if IsStringEmptyOrWhiteSpace(BillAmount) or IsBillNotValid(BillAmount):
        st.sidebar.error("Please provide Valid Number for Bill due")
        errors+=1

    if IsStringEmptyOrWhiteSpace(Name):
        st.sidebar.error("Please provide Customer Name") 
        errors+=1

    if IsStringEmptyOrWhiteSpace(PhoneNumber) or not IsValidPhoneNumber(PhoneNumber):
        st.sidebar.error("Please provide Valid Customer Phone number") 
        errors+=1

    if IsStringEmptyOrWhiteSpace(Email) or not IsValidEmail(Email):
        st.sidebar.error("Please provide Valid Email Id")   
        errors+=1
    
    if not IsStringEmptyOrWhiteSpace(Referrer):
        
        if not IdentifyPhoneNumberOrEmail_AndValidate_AndThrow(Referrer, "Referrer"):
            errors+=1
    
    return True if errors <= 0 else False

def RegisterCustomer(): 
    if ValidateCustomerFormData():

        customer = Customer(
            Name, PhoneNumber, Email, SpecialOccasion, Gender, 0, Referrer
        )
        allCustomerRecords = CustomerRecordService.GetAllCustomerRecord()
        highestCustomerId = 0
        errors = 0
        referrerFound = False
        referrerRowId = 0
        referrerCurrentWalletAmount = 0
        referrerId = 0

        #1. Validate the uniqueness of Customer PhoneNumber, Email
        #2. Validate if given Referrer exist
        for index, record in enumerate(allCustomerRecords):
            rowId = index + 2 #Starting index is 0, but on excel the first item stars from 2 (As Headers occupy 1)
            highestCustomerId = max(highestCustomerId, record[Constants.CustomerRecordColumnNameId])

            #Validate the uniqueness of Customer PhoneNumber
            if str(record[Constants.CustomerRecordColumnNamePhoneNumber]) == customer.PhoneNumber:
                st.sidebar.error(f"Customer Phone number {customer.PhoneNumber} already in Use.")
                errors += 1
            
            #Validate the uniqueness of Customer Email
            if record[Constants.CustomerRecordColumnNameEmail] == customer.Email:
                st.sidebar.error(f"Customer Email {customer.Email} already in Use.")
                errors += 1
            
            #Validate if given Referrer exist
            if customer.Referrer is not None and (customer.Referrer == record[Constants.CustomerRecordColumnNameEmail] or customer.Referrer == str(record[Constants.CustomerRecordColumnNamePhoneNumber])):
                referrerFound = True
                referrerRowId = rowId
                referrerCurrentWalletAmount = float(record[Constants.CustomerRecordColumnNameWallet])
                referrerName = record[Constants.CustomerRecordColumnNameName]
                referrerId = record[Constants.CustomerRecordColumnNameId]
        
        if customer.Referrer is not None and customer.Referrer.strip() is not "" and referrerFound is not True:
            st.sidebar.error(f"Provided Referrer does not exist.")
            errors += 1

        if errors == 0:
            customer.Id = highestCustomerId + 1
            CustomerRecordService.AddCustomerRecord(customer)
            st.sidebar.success(f"{Name} Registered! 😎")  

            customerSavings = float(BillAmount) * (Constants.DefaultJoiningBonus + Constants.DefaultReferrerBonus)
            st.success(f"{Name} saved {customerSavings}", icon = "🔥")

            if referrerFound:
                #Do discount calculations
                creditAmountToReferrer = Constants.DefaultReferrerBonus * float(BillAmount)
                referrerTotalWallet = referrerCurrentWalletAmount + creditAmountToReferrer
                
                #Credit the referrer's wallet
                CustomerRecordService.CreditCustomerWallet(referrerTotalWallet, referrerRowId)
                st.sidebar.success(f"Referrer {referrerName}'s wallet credited! 🥳")  

                #Track the Credit to referrer's wallet with its validity
                WalletCreditHistory.AddWalletRecordHistoryRecord(creditAmountToReferrer, referrerId)




#UI Form to accept Customer Data
with st.form(key = Constants.CustomerRegisterFormKey):
    Name = st.text_input(label = "Enter the Customer name")
    PhoneNumber = st.text_input(label = "Enter the Customer Phone number")
    Email = st.text_input(label = "Enter the Customer email")
    SpecialOccasion = st.date_input(label = "Provide a special occasion for customer", min_value=datetime(1950, 1, 1))
    Gender = st.selectbox("Provide the Customer gender", ("Male", "Female", "Others"))
    Referrer = st.text_input(label = "Enter the Referrer registered Email OR Phone Number (Optional)")
    BillAmount = st.text_input(label = "Enter current bill due for customer")
    Submit = st.form_submit_button(label = "Register Customer")

if Submit:
    RegisterCustomer()