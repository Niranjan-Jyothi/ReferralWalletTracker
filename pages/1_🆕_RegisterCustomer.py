import streamlit as st
import Constants
from Models.Customer import Customer as Customer
from datetime import datetime
from Utils.CommonValidators import IsStringEmptyOrWhiteSpace, IsValidEmail, IsValidPhoneNumber, IdentifyPhoneNumberOrEmail_AndValidate_AndThrow
import Services.CustomerRecordService as CustomerRecordService

st.title("Register new Customer!")


def ValidateCustomerFormData() -> bool:
    errors = 0

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

        #1. Validate the uniqueness of Customer PhoneNumber, Email
        #2. Validate if given Referrer exist
        for record in allCustomerRecords:
            highestCustomerId = max(highestCustomerId, record["Id"])

            #Validate the uniqueness of Customer PhoneNumber
            if str(record["PhoneNumber"]) == customer.PhoneNumber:
                st.sidebar.error(f"Customer Phone number {customer.PhoneNumber} already in Use.")
                errors += 1
            
            #Validate the uniqueness of Customer Email
            if record["Email"] == customer.Email:
                st.sidebar.error(f"Customer Email {customer.Email} already in Use.")
                errors += 1
            
            #Validate if given Referrer exist
            if customer.Referrer is not None and (customer.Referrer == record["Email"] or customer.Referrer == str(record["PhoneNumber"])):
                referrerFound = True
        
        if customer.Referrer is not None and customer.Referrer.strip() is not "" and referrerFound is not True:
            st.sidebar.error(f"Provided Referrer does not exist.")
            errors += 1

        if errors == 0:
            customer.Id = highestCustomerId + 1
            CustomerRecordService.AddCustomerRecord(customer)
            st.sidebar.success("Customer Registered!")  


#UI Form to accept Customer Data
with st.form(key = Constants.CustomerRegisterFormKey):
    Name = st.text_input(label = "Enter the Customer name")
    PhoneNumber = st.text_input(label = "Enter the Customer Phone number")
    Email = st.text_input(label = "Enter the Customer email")
    SpecialOccasion = st.date_input(label = "Provide a special occasion for customer", min_value=datetime(1950, 1, 1))
    Gender = st.selectbox("Provide the Customer gender", ("Male", "Female", "Others"))
    Referrer = st.text_input(label = "Enter the Referrer registered Email OR Phone Number (Optional)")
    Submit = st.form_submit_button(label = "Register Customer")

if Submit:
    RegisterCustomer()