from Models.WalletTransaction import WalletTransaction
from Providers.DataBaseConnection import GetSheetHandle
import Constants

walletTransactionSheetHandler = GetSheetHandle(Constants.WalletCreditHistorySheetName)

def AddWalletTransaction(walletRecord: WalletTransaction):
    if walletRecord.CustomerId > 0:
        walletTransactionSheetHandler.append_row(
            [walletRecord.CustomerId, walletRecord.Amount, walletRecord.TransactionType, walletRecord.TransactedAt, walletRecord.ValidUntil, walletRecord.Comment]
        )