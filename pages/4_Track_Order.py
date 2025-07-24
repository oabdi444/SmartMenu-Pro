import streamlit as st
import pandas as pd
from backend.db import get_connection
from streamlit_autorefresh import st_autorefresh

st.title("📦 Track Your Order")

# Auto-refresh every 5 seconds (5000 ms)
st_autorefresh(interval=5000, key="refresh")

table_number = st.text_input("Enter your table number to track your order:")

if table_number:
    conn = get_connection()
    df = pd.read_sql_query("SELECT item_name, quantity, status FROM orders WHERE table_number = ?", conn, params=(table_number,))
    conn.close()

    if df.empty:
        st.warning("No active orders found for this table.")
    else:
        st.subheader(f"Current Status for Table {table_number}")
        for _, row in df.iterrows():
            st.write(f"**{row['quantity']} x {row['item_name']}** — _Status: {row['status']}_")
            
        if all(row["status"] == "Delivered" for _, row in df.iterrows()):
            st.success("All items delivered. Enjoy your meal!")
