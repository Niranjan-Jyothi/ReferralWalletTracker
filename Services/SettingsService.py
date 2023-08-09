import Providers.SettingsProvider as SettingsProvider
import streamlit as st
from Models.Settings import Settings
import Constants as Constants

def ToSettingModel(data) -> Settings:
    return Settings(                  #-2 because excluding the headers + accommodating list starting from 0
        data[Constants.CreditedAmountValidityRowNumber - 2][Constants.SettingsValueColumnName], 
        data[Constants.ReferralBonusPercentageRowNumber - 2][Constants.SettingsValueColumnName])

@st.cache_data(max_entries=1, show_spinner= "Loading Settings..")
def FetchSettings() -> Settings:
    """Gets all Settings from Db

    Returns:
        Settings: Settings Model.
    """
    return ToSettingModel(SettingsProvider.GetAllSettings())

def UpdateSettingValues(newCreditedAmountValidity: int, newReferralBonusPercentage: float):
    """Updated the provided settings

    Args:
        newCreditedAmountValidity (int): Pass in the updated value for Credit Amount Validity (Days)
        newReferralBonusPercentage (float): Pass in the updated value for Referral Bonus Percentage (%)
    """
    SettingsProvider.ApplySettings(newCreditedAmountValidity, newReferralBonusPercentage)