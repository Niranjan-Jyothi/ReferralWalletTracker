import streamlit as st
import re

def IdentifyPhoneNumberOrEmail_AndValidate_AndThrow(input: str, entityName: str):
    if input.isnumeric() and not IsValidPhoneNumber(input):
        st.sidebar.error(f"Please provide Valid {entityName} Phone number") 
        return False

    elif not input.isnumeric() and not IsValidEmail(input):
        st.sidebar.error(f"Please provide Valid {entityName} Email/Phone number") 
        return False
    
    return True

def IsValidPhoneNumber(phone_number) -> bool:
    pattern = r"^\d{10}$"  # Assumes the phone number should have exactly 10 digits.
    return bool(re.match(pattern, phone_number))

def IsValidEmail(email) -> bool:
    pattern = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    return bool(re.match(pattern, email))

def IsStringEmptyOrWhiteSpace(input_string) -> bool:
    return input_string is None or input_string.strip() == ""