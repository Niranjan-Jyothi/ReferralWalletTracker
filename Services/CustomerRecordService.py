from Models.Customer import Customer
import Providers.CustomerRecordProvider as CustomerProvider

def AddCustomerRecord(customer: Customer):
    CustomerProvider.AddCustomerRecord(customer)

def GetAllCustomerRecord():
    return CustomerProvider.GetAllCustomerRecord()

def FindCustomerAndRowId_ByItem(searchItem: str):
    customerRow = CustomerProvider.FindCustomerIdByItem(searchItem)

    if customerRow > 0:
        return (CustomerProvider.FindCustomerByRowId(customerRow), customerRow)
    
    return (None, -1)

def DeleteCustomerByRowId(row : int):
    CustomerProvider.DeleteCustomerByRowId(row)

