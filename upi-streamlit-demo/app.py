import streamlit as st
import qrcode
import os
from PIL import Image
from upi_data import merchants, bank_balance, simulate_payment, txn_log

st.set_page_config(page_title="UPI Demo", page_icon="💸")
st.title("💸 UPI Payment Simulation Demo")

# Step 1: Merchant QR Code
merchant_name = st.selectbox("Select Merchant", list(merchants.keys()))
merchant_upi = merchants[merchant_name]

qr_path = f"qr_codes/{merchant_upi}.png"
os.makedirs("qr_codes", exist_ok=True)

if not os.path.exists(qr_path):
    qr = qrcode.make(f"upi://pay?pa={merchant_upi}&pn={merchant_name}")
    qr.save(qr_path)

st.subheader("📷 Scan this QR (simulated)")
st.image(Image.open(qr_path), width=200)

st.markdown("---")

# Step 2: Payment Input
with st.form("payment_form"):
    st.subheader("🔐 Enter Payment Details")
    payer = st.selectbox("Your UPI ID", ['raaj@paytm', 'aarti@paytm'])
    upi_pin = st.text_input("Enter UPI PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1, max_value=10000, step=1)

    submitted = st.form_submit_button("Pay Now")

    if submitted:
        success, message = simulate_payment(payer, upi_pin, merchant_upi, amount)
        if success:
            st.success(message)
        else:
            st.error(message)

        if success:
            st.markdown(f"💰 **Your Balance:** ₹{bank_balance[payer]}")
            st.markdown(f"🏪 **Merchant Balance:** ₹{bank_balance[merchant_upi]}")

st.markdown("---")
st.subheader("📄 Transaction Log")

if txn_log:
    for txn in reversed(txn_log[-5:]):
        st.markdown(f"- 💳 Txn ID `{txn['id']}`: ₹{txn['amount']} from **{txn['payer']}** to **{txn['payee']}**")
else:
    st.info("No transactions yet.")