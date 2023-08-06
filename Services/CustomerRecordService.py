from Models.Customer import Customer
import Providers.CustomerRecordProvider as CustomerProvider
import Constants

def AddCustomerRecord(customer: Customer):
    """Adds a new customer record.

    Args:
        customer (Customer): Pass in the Customer class.
    """
    CustomerProvider.AddCustomerRecord(customer)

def GetAllCustomerRecord():
    """Returns all customer records.

    Returns:
        List: Returns list of Customer's
    """
    return CustomerProvider.GetAllCustomerRecord()

def FindCustomerAndRowId_ByItem(searchItem: str):
    customerRow = CustomerProvider.FindCustomerIdByItem(searchItem)

    if customerRow > 1:
        return (CustomerProvider.FindCustomerByRowId(customerRow), customerRow)
    
    return (None, -1)

def DeleteCustomerByRowId(row : int):
    """Deletes a customer by its ROW number in DB.

    Args:
        row (int): Row value in the google sheet for which the entire row to be deleted.
    """
    #Preventing deletion of Admin
    if row > 2:
        CustomerProvider.DeleteCustomerByRowId(row)

def UpdateCustomerWallet(amount: int, customerRowId: int):
    """Updates Customer Wallet Column.

    Args:
        amount (int): Updated Wallet amount.
        customerRowId (int): ROW value of the customer as in the google sheet.
    """
    if customerRowId > 1:
        CustomerProvider.UpdateCustomerWallet(
            amount,
            customerRowId,
            Constants.CustomerRecordColumnNumberWallet
        )
