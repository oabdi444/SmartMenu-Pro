# SmartMenu Pro

SmartMenu Pro is a full-stack, real-time digital menu and restaurant order management system built with Streamlit and SQLite.

It replaces paper menus with a responsive digital interface for customers, provides a live kitchen dashboard for staff, and includes an admin panel for managing menu items and orders. The project is modular, database-backed, and production-ready.

---

## Features

### Customer Menu
- Interactive digital menu with categories and descriptions
- Cart functionality with quantity selection
- Order submission tied to table numbers
- Designed for tablet or QR-based access

### Kitchen Dashboard
- Real-time view of all active orders grouped by table
- Update order statuses: Pending, In Progress, Ready, Delivered
- Automatic syncing with customer tracking view

### Admin Panel
- Add, update, or remove menu items
- Manage inventory and stock levels
- Clear daily orders
- Automatically seeds sample menu on first launch

### Real-Time Order Tracking
- Customers can enter their table number to view live order statuses
- Auto-refreshes every few seconds for real-time updates

---

## Tech Stack

| Layer     | Technology                 |
|-----------|-----------------------------|
| Frontend  | Streamlit                   |
| Backend   | SQLite (Python's `sqlite3`) |
| Data Handling | pandas                  |
| Utilities | Pillow, qrcode, streamlit-authenticator, streamlit-autorefresh |

---

## Project Structure

smartmenu-pro/
│
├── app.py # Main entry point
├── config.py # App title, icon, layout
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── backend/
│ ├── db.py # Database initialization and connection
│ └── utils.py # (optional) reusable utilities
│
├── data/
│ └── database.db # SQLite database (auto-generated)
│
├── pages/
│ ├── 1_Menu.py # Customer digital menu and cart
│ ├── 2_Kitchen.py # Kitchen order management dashboard
│ ├── 3_Admin.py # Admin interface for menu and stock
│ └── 4_Track_Order.py # Real-time customer order status view

yaml
Copy
Edit

---

## Installation and Running Locally

1. Clone the repository

```bash
git clone https://github.com/oabdi444/smartmenu-pro.git
cd smartmenu-pro

python -m venv venv
source venv/bin/activate        # On Windows: .\venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

This project is licensed under the MIT License.

