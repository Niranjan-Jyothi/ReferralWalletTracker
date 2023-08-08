import streamlit as st
from UIComponents.LoginPage import IsUserAuthenticated

if IsUserAuthenticated():

    st.title("Insights💡")
    st.warning("This feature is under development")