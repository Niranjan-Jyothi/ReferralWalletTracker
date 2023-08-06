import streamlit as st
import Constants

st.title("Settings ⚙️")

if Constants.CreditAmountValidityKey not in st.session_state:
    st.session_state[Constants.CreditAmountValidityKey] = Constants.DefaultCreditAmountValidity

def ApplyNewSettings():
    st.session_state[Constants.CreditAmountValidityKey] = int(newCreditValidityDays)
    st.success("Settings Applied")
    st.warning("Applied changes only apply to this session! They will be restored to default later on.")

with st.form(key = "ChangeSettingsForm"):
    newCreditValidityDays = st.number_input(label="Credit amount Validity (in DAYS)", value=st.session_state[Constants.CreditAmountValidityKey], min_value=10, max_value=200)
    submitButton = st.form_submit_button(label="Apply Settings")

if submitButton:
    ApplyNewSettings()