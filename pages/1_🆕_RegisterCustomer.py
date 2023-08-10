import streamlit as st
from UIComponents.LoginPage import IsUserAuthenticated

if IsUserAuthenticated():

    import Constants
    from Models.Customer import Customer as Customer
    from datetime import datetime
    from Utils.CommonValidators import *
    from Services import CustomerRecordService, WalletTransactionService, SettingsService

    st.title("Register new Customer!")

    def CalculateJoiningOrReferrerCreditAmount(bonusPercentage, totalAmount) -> float:
        """Calculates the Joining or Referrer Amount

        Args:
            bonusPercentage (_type_): Percentage Increase
            totalAmount (_type_): Total Bill from which percentage is taken for Wallet credit

        Returns:
            float: Amount to be credited.
        """
        bonus = bonusPercentage/100
        return float(totalAmount) * bonus


    def ValidateCustomerFormData() -> bool:
        errors = 0

        if IsStringEmptyOrWhiteSpace(BillAmount) or IsBillNotValid(BillAmount):
            st.sidebar.error("Please provide valid Bill Amount.")
            errors+=1

        if IsStringEmptyOrWhiteSpace(Name):
            st.sidebar.error("Please provide Customer Name") 
            errors+=1

        if IsStringEmptyOrWhiteSpace(PhoneNumber) or not IsValidPhoneNumber(PhoneNumber):
            st.sidebar.error("Please provide Valid Customer Phone number") 
            errors+=1

        if IsStringEmptyOrWhiteSpace(Email) or not IsValidEmail(Email):
            st.sidebar.error("Please provide Valid Email Id")   
            errors+=1
        
        if not IsStringEmptyOrWhiteSpace(Referrer):
            
            if not IdentifyPhoneNumberOrEmail_AndValidate_AndThrow(Referrer, "Referrer"):
                errors+=1
        
        return True if errors <= 0 else False

    @st.cache_data(ttl=120, max_entries=2, show_spinner= "Validating Customer..")
    def GetAllCachedCustomerRecords():
        return CustomerRecordService.GetAllCustomerRecord()

    def RegisterCustomer():
        if ValidateCustomerFormData():

            customer = Customer(
                Name, PhoneNumber, Email, SpecialOccasion, SpecialOccasionType, Gender, 0, Referrer
            )
            allCustomerRecords = GetAllCachedCustomerRecords()
            highestCustomerId = 0
            errors = 0
            referrerFound = False
            referrerRowId = 0
            referrerCurrentWalletAmount = 0
            referrerCustomerId = None

            #1. Validate the uniqueness of Customer PhoneNumber, Email
            #2. Validate if given Referrer exist
            for index, record in enumerate(allCustomerRecords):
                rowId = index + 2 #Starting index is 0, but on excel the first item stars from 2 (As Headers occupy 1)
                highestCustomerId = max(highestCustomerId, record[Constants.CustomerRecordColumnNameId])

                #Validate the uniqueness of Customer PhoneNumber
                if str(record[Constants.CustomerRecordColumnNamePhoneNumber]) == customer.PhoneNumber:
                    st.sidebar.error(f"Customer Phone number {customer.PhoneNumber} already in Use.")
                    errors += 1
                
                #Validate the uniqueness of Customer Email
                if record[Constants.CustomerRecordColumnNameEmail] == customer.Email:
                    st.sidebar.error(f"Customer Email {customer.Email} already in Use.")
                    errors += 1
                
                #Validate if given Referrer exist
                if customer.Referrer is not None and (customer.Referrer == record[Constants.CustomerRecordColumnNameEmail] or customer.Referrer == str(record[Constants.CustomerRecordColumnNamePhoneNumber])):
                    referrerFound = True
                    referrerRowId = rowId
                    referrerCurrentWalletAmount = float(record[Constants.CustomerRecordColumnNameWallet])
                    referrerName = record[Constants.CustomerRecordColumnNameName]
                    referrerCustomerId = record[Constants.CustomerRecordColumnNameId]

            if customer.Referrer is not None and customer.Referrer.strip() is not "" and referrerFound is not True:
                st.sidebar.error(f"Provided Referrer does not exist.")
                errors += 1

            if errors == 0:
                customer.Id = highestCustomerId + 1  #New customer ID
                customer.Referrer = referrerCustomerId #We store the referrer's Id instead of their Phone/Email for optimization
                
                currentSettings_ReferralBonusPercentage = SettingsService.FetchSettings().ReferralBonusPercentage #NOTE: We will use Referral bonus percentage also for newly joined Customer percentage
                customer.Wallet = CalculateJoiningOrReferrerCreditAmount(currentSettings_ReferralBonusPercentage, BillAmount) # New customer gets joining bonus credited to their wallet.
                
                CustomerRecordService.AddCustomerRecord(customer) #NOTE: API 1
                st.sidebar.success(f"{Name} Registered with a Wallet total of {customer.Wallet}! 😎")  
                
                GetAllCachedCustomerRecords.clear()
                
                #Track the Credit to just joined customers wallet
                WalletTransactionService.AddWalletCreditRecord(customer.Wallet, customer.Id, "Credited as Joining bonus") #NOTE: API 2

                if referrerFound:
                    #Calculate earnings for referrer.
                    creditAmountToReferrer = CalculateJoiningOrReferrerCreditAmount(currentSettings_ReferralBonusPercentage, BillAmount)
                    referrerTotalWallet = referrerCurrentWalletAmount + creditAmountToReferrer
                    
                    #Credit the referrer's wallet
                    CustomerRecordService.UpdateCustomerWallet(referrerTotalWallet, referrerRowId) #NOTE: API 3
                    st.sidebar.success(f"Referrer {referrerName}'s wallet credited! 🥳")  

                    #Track the Credit to referrer's wallet with its validity
                    WalletTransactionService.AddWalletCreditRecord(creditAmountToReferrer, referrerCustomerId, "Credited as Referrer bonus") #NOTE: API 4



    #UI Form to accept Customer Data
    with st.form(key = Constants.CustomerRegisterFormKey):
        Name = st.text_input(label = "Enter the Customer name")
        PhoneNumber = st.text_input(label = "Enter the Customer Phone number")
        Email = st.text_input(label = "Enter the Customer email")
        SpecialOccasion = st.date_input(label = "Provide a special occasion for customer", min_value=datetime(1950, 1, 1))
        SpecialOccasionType = st.selectbox("Whats the special occasion for ?", ("Birthday 🎂", "Anniversary 💑", "Others"))
        Gender = st.selectbox("Provide the Customer gender", ("Male", "Female", "Others"))
        Referrer = st.text_input(label = "Enter the Referrer registered Email OR Phone Number (Optional)")
        BillAmount = st.text_input(label = "Enter Bill Amount")
        Submit = st.form_submit_button(label = "Register Customer")

    if Submit:
        RegisterCustomer()