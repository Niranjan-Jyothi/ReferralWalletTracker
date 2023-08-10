from Models.WalletTransaction import WalletTransaction
import Providers.WalletTransactionProvider as WalletTransactionProvider

def AddWalletCreditRecord(creditedAmount: float, customerId: int, reasonForCredit: str):
    if customerId > 0:
        walletRecordTrack = WalletTransaction(customerId, creditedAmount, True, reasonForCredit, True) #Every new credit is valid until its Credit Validity tenure, during which the maintainance will make it InValid
        WalletTransactionProvider.AddWalletTransaction(walletRecordTrack)

def AddWalletDebitRecord(debitAmount: float, customerId: int):
    if customerId > 0:
        walletRecordTrack = WalletTransaction(customerId, debitAmount, False, "Redeemed", False)
        WalletTransactionProvider.AddWalletTransaction(walletRecordTrack)

def GetAllTransactions():
    return WalletTransactionProvider.GetAllTransactions()
