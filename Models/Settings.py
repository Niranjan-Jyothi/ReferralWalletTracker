import Utils.Utilities as Utils
import Constants as Constants

class Settings():
    """Class that represents the Configuration/Settings of the App.
    """
    def __init__(self, creditedAmountValidity, referralBonusPercentage):
        """Constructor of Settings Class: A Class that represents the Configuration/Settings of the App.

        Args:
            creditedAmountValidity (string): Credited amount Validity in 'DAYS'; Value Should be int parsable.
            referralBonusPercentage (string): Percentage(in %) Bonus for referrer; Value should be float parsable.
        """
        _, self.CreditedAmountValidity = Utils.TryParseInt(creditedAmountValidity, Constants.DefaultCreditAmountValidity)
        _, self.ReferralBonusPercentage = Utils.TryParseFloat(referralBonusPercentage, Constants.DefaultReferrerBonus * 100)