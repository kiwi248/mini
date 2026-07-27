import streamlit as st
from streamlit_session_browser_storage import SessionStorage


st.set_page_config(
    page_title="목차",
    page_icon="😀",
    layout="wide",
)

ykw_pizza_page = st.Page("app_pages/ykw/pizza.py", url_path="ykw_pizza", default=True)
ykw_select_page = st.Page("app_pages/ykw/select.py", url_path="ykw_select")
ykw_survey_page = st.Page("app_pages/ykw/survey.py", url_path="ykw_survey")

sym_select_page = st.Page("app_pages/sym/chattable.py", url_path="sym_select")
sym_pizza_page = st.Page("app_pages/sym/pizza.py", url_path="sym_pizza")
sym_survey_page = st.Page("app_pages/sym/survey.py", url_path="sym_survey")

port_select_page = st.Page("app_pages/port/charttable.py", url_path="port_select")
port_pizza_page = st.Page("app_pages/port/pizza.py", url_path="port_pizza")
port_survey_page = st.Page("app_pages/port/survey.py", url_path="port_survey")




pages = [ykw_pizza_page, ykw_select_page, ykw_survey_page,
         sym_select_page, sym_pizza_page, sym_survey_page,
         port_select_page, port_pizza_page, port_survey_page]



navigation = st.navigation(pages, position="hidden")

with st.sidebar:
    st.info("목차 페이지")
    st.divider()
    st.page_link(ykw_pizza_page, label="😀 ykw Pizza")
    st.page_link(ykw_select_page, label="😀 ykw Select")
    st.page_link(ykw_survey_page, label="😀 ykw Survey")
    st.page_link(sym_pizza_page, label="😀 sym Pizza")
    st.page_link(sym_select_page, label="😀 sym Select")
    st.page_link(sym_survey_page, label="😀 sym Survey")
    st.page_link(port_pizza_page, label="😀 port Pizza")
    st.page_link(port_select_page, label="😀 port Select")
    st.page_link(port_survey_page, label="😀 port Survey")


navigation.run()
