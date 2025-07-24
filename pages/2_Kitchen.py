import streamlit as st
import pandas as pd
from backend.db import get_connection

st.title("👨‍🍳 Kitchen Dashboard")

conn = get_connection()
orders_df = pd.read_sql_query("SELECT * FROM orders WHERE status != 'Delivered'", conn)

if orders_df.empty:
    st.info("No orders.")
else:
    for table in orders_df['table_number'].unique():
        st.subheader(f"Table {table}")
        table_orders = orders_df[orders_df['table_number'] == table]
        for _, row in table_orders.iterrows():
            col1, col2, col3 = st.columns([3, 1, 2])
            with col1:
                st.write(f"{row['quantity']} x {row['item_name']}")
            with col2:
                new_status = st.selectbox("Update Status", ["Pending", "In Progress", "Ready", "Delivered"], index=["Pending", "In Progress", "Ready", "Delivered"].index(row['status']), key=row['id'])
            with col3:
                if st.button("Save", key=f"save_{row['id']}"):
                    cursor = conn.cursor()
                    cursor.execute("UPDATE orders SET status = ? WHERE id = ?", (new_status, row['id']))
                    conn.commit()
                    st.success("Status updated.")
conn.close()
