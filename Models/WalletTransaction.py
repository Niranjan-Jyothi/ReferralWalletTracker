from datetime import date, timedelta
import Constants

class WalletTransaction():
    """ A class representing a Wallet Transaction record.. 
        It could be either amount credited or debited (Redeemed)
        This also holds the Validity of a credited amount.    """

    def __init__(self, customerId, amount, isCredited: bool, comment) -> None:
        self.CustomerId: int = int(customerId)
        self.Amount: int = float(amount)
        self.TransactedAt: date = date.today().strftime(Constants.DateTimeFormat)
        self.TransactionType = "Credited" if isCredited else "Debited"
        self.ValidUntil: date = self.GetCreditedAmountValidity() if isCredited else None
        self.Comment = comment

    def GetCreditedAmountValidity(self) -> date:
        return (date.today() + timedelta(days=Constants.DefaultCreditAmountValidity)).strftime(Constants.DateTimeFormat)