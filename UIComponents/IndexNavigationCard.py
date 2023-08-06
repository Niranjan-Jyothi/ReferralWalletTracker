from streamlit_card import card
import streamlit as st
from streamlit_extras.switch_page_button import switch_page


def NavigateToRegisterCustomerPage():
    switch_page("RegisterCustomer")

def NavigateToSettingsPage():
    switch_page("Settings")

def NavigateToInsightsPage():
    switch_page("Insights")

###SHOULD CACHE THIS?
def ShowNavigationCardsOnUI():

    (cardColumn1, cardColumn2) = st.columns([1,1])

    with cardColumn1:
        card(
            title="",
            text="Register new customer",
            image="https://plus.unsplash.com/premium_photo-1661757369657-d7b09363e137?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
            url=None,
            on_click = NavigateToRegisterCustomerPage
        )

    with cardColumn2:
        card(
            title="",
            text="Goto Settings ⚙️",
            image="https://images.unsplash.com/photo-1627415861814-eccd21072157?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80",
            url=None,
            on_click = NavigateToSettingsPage
        )

    card(
        title="",
        text="See Insights 💡",
        image="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
        url=None,
        on_click = NavigateToInsightsPage
    )