import streamlit as st
import pandas as pd
from backend.db import get_connection

st.title("🛠️ Admin Panel")

conn = get_connection()
menu_df = pd.read_sql_query("SELECT * FROM menu", conn)

st.subheader("Add New Menu Item")
with st.form("new_item"):
    name = st.text_input("Name")
    description = st.text_area("Description")
    category = st.text_input("Category")
    price = st.number_input("Price", min_value=0.0)
    stock = st.number_input("Stock", min_value=0)
    submitted = st.form_submit_button("Add Item")
    if submitted:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menu (name, description, category, price, stock) VALUES (?, ?, ?, ?, ?)",
                       (name, description, category, price, stock))
        conn.commit()
        st.success("Menu item added.")

st.subheader("Current Menu")
st.dataframe(menu_df)

if st.button("Clear All Orders"):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders")
    conn.commit()
    st.success("All orders cleared.")

conn.close()
