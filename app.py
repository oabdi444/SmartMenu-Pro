import streamlit as st
from backend.db import init_db
from config import PAGE_TITLE, PAGE_ICON

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
init_db()

st.title("SmartMenu Pro — Digital Menu & Kitchen System")
st.info("Use the sidebar to navigate: Menu | Kitchen | Admin")
