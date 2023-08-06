from Models.WalletTransaction import WalletTransaction
import Providers.WalletTransactionProvider as WalletTransactionProvider

def AddWalletCreditRecord(creditedAmount: float, customerId: int):
    if customerId > 0:
        walletRecordTrack = WalletTransaction(customerId, creditedAmount, True, "Credited as Referrer bonus")
        WalletTransactionProvider.AddWalletTransaction(walletRecordTrack)

def AddWalletDebitRecord(debitAmount: float, customerId: int):
    if customerId > 0:
        walletRecordTrack = WalletTransaction(customerId, debitAmount, False, "Redeemed")
        WalletTransactionProvider.AddWalletTransaction(walletRecordTrack)
