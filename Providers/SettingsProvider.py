import Constants
from Providers.DataBaseConnection import GetSheetHandle
import streamlit as st

settingsSheetHandler = GetSheetHandle(Constants.SettingsSheetName)

def GetAllSettings():
    """Gets all Settings from Db

    Returns:
        List: List of configured Settings; Eg record: [1, CreditedAmountValidity, 60]
    """
    return settingsSheetHandler.get_all_records()

def ApplySettings(newCreditedAmountValidity: int, newReferralBonusPercentage: float):
    """Updates Settings sheet with provided list of values onto provided Column range.

     Args:
        newCreditedAmountValidity (int): Pass in the updated value for Credit Amount Validity (Days)
        newReferralBonusPercentage (float): Pass in the updated value for Referral Bonus Percentage (%)
    """
    
    settingsSheetHandler.batch_update([
        {
            'range': Constants.SettingCreditedAmountValidityValueCell,
            'values': [[newCreditedAmountValidity]],
        },
        {
            'range': Constants.SettingReferralBonusPercentageValueCell,
            'values': [[newReferralBonusPercentage]],
        }
    ])