from Models.WalletRecord import WalletRecord
import Providers.CustomerRecordProvider as CustomerProvider

def AddWalletRecordHistoryRecord(creditedAmount: float, customerId: int):
    if customerId > 0:
        walletRecordTrack = WalletRecord(customerId, creditedAmount, "Credited as Referrer bonus")
        CustomerProvider.AddWalletCreditRecord(walletRecordTrack)
