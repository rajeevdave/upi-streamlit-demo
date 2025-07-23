Step-by-Step: UPI Demo App
Step 1: Install dependencies
pip install streamlit qrcode[pil] pillow
Step 2: Project Structure

upi-streamlit-demo/
├── app.py
├── upi_data.py         ← optional helper for cleaner code
└── qr_codes/           ← auto-created folder for QR images

✅ QR generation
✅ Simulated UPI payment
✅ PIN check
✅ Multiple merchants (selectable)
✅ Transaction log
✅ Clean UI for demo use

Step 4: Run the App

streamlit run app.py

Feature	Description
🧾 QR Code	Auto-generated for merchants
🧍 UPI ID select	Payer can choose UPI
🔐 PIN	Simulated UPI PIN entry
💰 Balance check	Instant debit/credit
📊 Txn log	Last 5 transactions shown
🌐 UI	Web-based, interactive, great for demo sessions

