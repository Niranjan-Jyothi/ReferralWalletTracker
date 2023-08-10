from datetime import date, timedelta
import Constants
import Services.SettingsService as SettingsService

class WalletTransaction():
    """ A class representing a Wallet Transaction record.. 
        It could be either amount credited or debited (Redeemed)
        This also holds the Validity of a credited amount.    """

    def __init__(self, customerId, amount, isCredited: bool, comment, isValid: bool) -> None:
        self.CustomerId: int = int(customerId)
        self.Amount: int = float(amount)
        self.TransactedAt: date = date.today().strftime(Constants.DateTimeFormat)
        self.TransactionType = "Credited" if isCredited else "Debited"
        self.ValidUntil: date = self.GetCreditedAmountValidity() if isCredited else None
        self.Comment = comment
        self.IsValid = isValid

    def GetCreditedAmountValidity(self) -> date:
        settings = SettingsService.FetchSettings()
        
        return (date.today() + timedelta(days = settings.CreditedAmountValidity)).strftime(Constants.DateTimeFormat)
    