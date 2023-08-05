from Models.WalletTransaction import WalletTransaction
import Providers.CustomerRecordProvider as CustomerProvider

def AddWalletRecordHistoryRecord(creditedAmount: float, customerId: int):
    if customerId > 0:
        walletRecordTrack = WalletTransaction(customerId, creditedAmount, True, "Credited as Referrer bonus")
        CustomerProvider.AddWalletTransaction(walletRecordTrack)
