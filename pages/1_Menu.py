import streamlit as st
import pandas as pd
from backend.db import get_connection

st.title("📋 Menu")

conn = get_connection()
menu_df = pd.read_sql_query("SELECT * FROM menu WHERE stock > 0", conn)
conn.close()

if menu_df.empty:
    st.warning("No items available.")
else:
    cart = {}
    for _, row in menu_df.iterrows():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader(row['name'])
            st.caption(row['description'])
        with col2:
            qty = st.number_input(f"Qty - {row['name']}", min_value=0, max_value=row['stock'], step=1)
            if qty > 0:
                cart[row['name']] = qty

    table_number = st.text_input("Table Number")

    if st.button("Place Order") and cart and table_number:
        conn = get_connection()
        cursor = conn.cursor()
        for item, quantity in cart.items():
            cursor.execute("INSERT INTO orders (table_number, item_name, quantity, status) VALUES (?, ?, ?, ?)",
                           (table_number, item, quantity, "Pending"))
        conn.commit()
        conn.close()
        st.success("Order submitted to the kitchen.")
