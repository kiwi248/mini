import streamlit as st
from streamlit_session_browser_storage import SessionStorage


st.set_page_config(
    page_title="Layout",
    page_icon="😀",
    layout="wide",
)

home_page = st.Page("app_pages/01_home.py", default=True)
login_page = st.Page("app_pages/00_login.py")
signup_page = st.Page("app_pages/02_signup.py")


pages = [home_page, login_page, signup_page]



navigation = st.navigation(pages, position="hidden")

with st.sidebar:
    st.info("화면왼쪽")
    st.divider()
    st.page_link(home_page, label="😀 HOME")
    st.page_link(login_page, label="😀 Sign In")
    st.page_link(signup_page, label="😀 Sign Up")


navigation.run()
