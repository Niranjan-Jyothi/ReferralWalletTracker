import streamlit as st
import Constants
import streamlit_authenticator as stauth

ValidUsers = st.secrets[Constants.Secrets_ValidCredentialsKey]
UserAuthCookieConfig = st.secrets['UserAuthCookieConfig']
CookieName = UserAuthCookieConfig[Constants.Secrets_CookieName]
SignatureKey = UserAuthCookieConfig[Constants.Secrets_SignatureKey]
CookieExpiration = UserAuthCookieConfig[Constants.Secrets_CookieExpiration]

#---Expected format by Streamlit-----
# cred = {
#     'usernames': {
#         'jsmith' : {
#             'password' : jSmaith's passowrd Hashed,
#             'name' : jSmaith,
#             'email : j.S@gmail.com
#         }
#     }
# }
credentials = {
    "usernames" : { 
            user['UserName'] : {   
                'password' : user['Password'], 
                'name' : user['UserName']} for user in ValidUsers}}

@st.cache_resource(show_spinner = "Signing in..", experimental_allow_widgets=True)
def GetAuthenticator():
    return stauth.Authenticate(credentials, CookieName, SignatureKey, CookieExpiration)

def RenderLoginComponent() -> bool:
    authenticator = stauth.Authenticate(credentials, CookieName, SignatureKey, CookieExpiration)
    name, authentication_status, username = authenticator.login('Login', 'main')
    
    if authentication_status:
        authenticator.logout("logout", 'sidebar')
        return True
    
    elif authentication_status is False:
        st.error('Incorrect credentials.')
        return False

    elif authentication_status is None:
        st.warning('Please enter your username and password.')
        return False

    return False

def IsUserAuthenticated() -> bool:
    if "authentication_status" not in st.session_state:
        return RenderLoginComponent()
    
    elif st.session_state["authentication_status"]:
        authenticator = GetAuthenticator()
        authenticator.logout("logout", 'sidebar')
        return True
    
    return RenderLoginComponent()