from UIComponents.LoginPage import IsUserAuthenticated

if IsUserAuthenticated():

    import streamlit as st
    import Services.SettingsService as SettingsService

    st.title("Settings ⚙️")    

    FetchedSettings = SettingsService.FetchSettings()

    with st.form(key = "ChangeSettingsForm"):
        newCreditValidityDays = st.number_input(label="Credit amount Validity (in DAYS)", value=FetchedSettings.CreditedAmountValidity, min_value=10, max_value=300)
        newReferrerBonus = st.number_input(label="Referrer Bonus (in %)", value=FetchedSettings.ReferralBonusPercentage, min_value=0.0, max_value=100.0, step=0.5)
        submitButton = st.form_submit_button(label="Apply Settings")

    if submitButton:
        SettingsService.UpdateSettingValues(  # Update values
            newCreditValidityDays,   
            newReferrerBonus
        )
        SettingsService.FetchSettings.clear() # Clear cache
        st.success("Settings Applied")