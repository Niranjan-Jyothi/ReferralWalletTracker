import streamlit as st
from Models.Customer import Customer
from datetime import datetime
import Providers.CustomerRecordProvider as CustomerProvider
import Constants

def GetSafeFromList(list, index):
    try:
        return list[index]
    except IndexError:
        return None

def ToCustomer(record):
    """Converts the Fetched Google sheet record row into Customer Object

    Args:
        record (List): List of Customer properties that correspond to their column values in Google sheet

    Returns:
        Customer: Customer Object
    """

    return Customer(
        GetSafeFromList(record, Constants.CustomerRecordColumnNumber_Name - 1),
        GetSafeFromList(record, Constants.CustomerRecordColumnNumber_PhoneNumber - 1),
        GetSafeFromList(record, Constants.CustomerRecordColumnNumber_Email - 1),
        datetime.strptime(GetSafeFromList(record, Constants.CustomerRecordColumnNumber_SpecialOccasion - 1), Constants.DateTimeFormat),
        GetSafeFromList(record, Constants.CustomerRecordColumnNumber_SpecialOccasionType - 1),
        GetSafeFromList(record, Constants.CustomerRecordColumnNumber_Gender - 1),
        GetSafeFromList(record, Constants.CustomerRecordColumnNumber_Wallet - 1),
        GetSafeFromList(record, Constants.CustomerRecordColumnNumber_Referrer - 1),
        GetSafeFromList(record, Constants.CustomerRecordColumnNumber_Id - 1),
    )

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

def FindCustomerAndRowId_ByItem(searchItem: str) -> (Customer, int):
    customerRow = CustomerProvider.FindCustomerRowIdByItem(searchItem)

    if customerRow > 1:
        return (ToCustomer(CustomerProvider.FindCustomerByRowId(customerRow)), customerRow)
    
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
            Constants.CustomerRecordColumnNumber_Wallet
        )
