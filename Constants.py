CustomerRegisterFormKey = "customerRegisterForm"

DateTimeFormat = '%d/%m/%Y'

#DB and Sheet Names
GoogleSheetDbName = "CustomerDB"
CustomerSpreadSheetName = "Customer"
WalletCreditHistorySheetName = "WalletTransaction"
SettingsSheetName = "Settings"

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

#Google sheet Column Name Mapping for Settings Sheet
SettingCreditedAmountValidityValueCell = 'C2'
SettingReferralBonusPercentageValueCell = 'C3'
SettingsValueColumnName = "SettingsValue"

#Google sheet Column Number Mapping for Settings Sheet
CreditedAmountValidityRowNumber = 2
ReferralBonusPercentageRowNumber = 3

#Secrets Keys
Secrets_ValidCredentialsKey = "PermittedCredentials"
Secrets_UserAuthCookieConfig = "UserAuthCookieConfig"
Secrets_GoogleApiKey = "gcp_service_account"
Secrets_CookieName = "CookieName"
Secrets_SignatureKey = "SignatureKey"
Secrets_CookieExpiration = "CookieExpiration"

#Settings
DefaultJoiningBonus = 0.05 #5%   ----------- Not used
DefaultSeasonalBonus = 0.1 #10%  ----------- Not used

DefaultCreditAmountValidity = 60 #In days
DefaultReferrerBonus = 0.1 #10%

