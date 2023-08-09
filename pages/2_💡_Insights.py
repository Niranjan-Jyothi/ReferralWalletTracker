import streamlit as st
from UIComponents.LoginPage import IsUserAuthenticated

@st.cache_data(ttl=120, max_entries=2, show_spinner= "Gathering insights..")
def GetAllCachedCustomersAsDataFrame():
    return DataFrame(CustomerRecordService.GetAllCustomerRecord())

if IsUserAuthenticated():
    from streamlit_extras.dataframe_explorer import dataframe_explorer
    import Services.CustomerRecordService as CustomerRecordService
    from pandas import DataFrame
    
    st.title("Insights💡")
    st.warning("This is just a preview. Feature is under development.")

    dataframe = GetAllCachedCustomersAsDataFrame()
    filtered_df = dataframe_explorer(dataframe, case=False) # Filter is using Streamlit magic
    st.dataframe(filtered_df, use_container_width=True) # Display it