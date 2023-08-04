from datetime import date, datetime, timedelta
import Constants

class WalletRecord():
    """ A class representing a Wallet credit/Debit record. """
    
    def __init__(self, customerId, creditedAmount, comment) -> None:
        self.CustomerId: int = int(customerId)
        self.CreditedAmount: int = float(creditedAmount)
        self.Comment = comment
        self.CreditedAt: date = date.today().strftime(Constants.DateTimeFormat)
        self.ValidUntil: date = (date.today() + timedelta(days=Constants.DefaultCreditAmountValidity)).strftime(Constants.DateTimeFormat)