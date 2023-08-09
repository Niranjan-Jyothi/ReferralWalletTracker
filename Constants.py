CustomerRegisterFormKey = "customerRegisterForm"

DateTimeFormat = '%d/%m/%Y'

#DB and Sheet Names
GoogleSheetDbName = "CustomerDB"
CustomerSpreadSheetName = "Customer"
WalletCreditHistorySheetName = "WalletTransaction"

#Google sheet Column Number mapping
CustomerRecordColumnNumber_Id = 1
CustomerRecordColumnNumber_Name = 2
CustomerRecordColumnNumber_Gender = 3
CustomerRecordColumnNumber_Wallet = 4
CustomerRecordColumnNumber_PhoneNumber = 5
CustomerRecordColumnNumber_Email = 6
CustomerRecordColumnNumber_RegisteredAt = 7
CustomerRecordColumnNumber_SpecialOccasion = 8
CustomerRecordColumnNumber_SpecialOccasionType = 9
CustomerRecordColumnNumber_Referrer = 10

#Google sheet Column Number mapping
CustomerRecordColumnNameWallet = "Wallet"
CustomerRecordColumnNamePhoneNumber = "PhoneNumber"
CustomerRecordColumnNameEmail = "Email"
CustomerRecordColumnNameName = "Name"
CustomerRecordColumnNameId = "Id"
CustomerRecordColumnNameSpecialOccasionType = "SpecialOccasionType"
CustomerRecordColumnNameSpecialOccasion = "SpecialOccasion"

#Secrets Keys
Secrets_ValidCredentialsKey = "PermittedCredentials"
Secrets_UserAuthCookieConfig = "UserAuthCookieConfig"
Secrets_GoogleApiKey = "gcp_service_account"
Secrets_CookieName = "CookieName"
Secrets_SignatureKey = "SignatureKey"
Secrets_CookieExpiration = "CookieExpiration"

#Settings
DefaultReferrerBonus = 0.1 #10%
DefaultJoiningBonus = 0.05 #5%
DefaultSeasonalBonus = 0.1 #10%

ReferrerBonusKey = "ReferrerBonus"

DefaultCreditAmountValidity = 60 #In days
CreditAmountValidityKey = "CreditAmountValidity"