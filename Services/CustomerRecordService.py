from Models.Customer import Customer
import Providers.CustomerRecordProvider as CustomerProvider
import Constants

def AddCustomerRecord(customer: Customer):
    CustomerProvider.AddCustomerRecord(customer)

def GetAllCustomerRecord():
    return CustomerProvider.GetAllCustomerRecord()

def FindCustomerAndRowId_ByItem(searchItem: str):
    customerRow = CustomerProvider.FindCustomerIdByItem(searchItem)

    if customerRow > 1:
        return (CustomerProvider.FindCustomerByRowId(customerRow), customerRow)
    
    return (None, -1)

def DeleteCustomerByRowId(row : int):
    #Preventing deletion of Admin
    if row > 2:
        CustomerProvider.DeleteCustomerByRowId(row)

def CreditCustomerWallet(amount: int, customerRowId: int):
    if customerRowId > 1:
        CustomerProvider.UpdateCustomerWallet(
            amount,
            customerRowId,
            Constants.CustomerRecordColumnNumberWallet
        )
