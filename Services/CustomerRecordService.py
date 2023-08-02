from Models.Customer import Customer
import Providers.CustomerRecordProvider as CustomerProvider

def AddCustomerRecord(customer: Customer):
    CustomerProvider.AddCustomerRecord(customer)

def GetAllCustomerRecord():
    return CustomerProvider.GetAllCustomerRecord()

