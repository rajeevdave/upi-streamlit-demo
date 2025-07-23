import uuid

# Simulated user and merchant balances
bank_balance = {
    'raaj@paytm': 500,
    'aarti@paytm': 300,
    'rahul@upi': 100,
    'chaiwala@upi': 150
}

# UPI PINs (for demo only)
upi_pins = {
    'raaj@paytm': '1234',
    'aarti@paytm': '4321'
}

# Merchants
merchants = {
    "Rahul's Tea Stall": 'rahul@upi',
    "Chai Wala": 'chaiwala@upi'
}

# Transaction log
txn_log = []

def simulate_payment(payer, pin, payee, amount):
    if payer not in bank_balance or payee not in bank_balance:
        return False, "❌ Invalid UPI ID."

    if upi_pins.get(payer) != pin:
        return False, "🔒 Incorrect UPI PIN."

    if bank_balance[payer] < amount:
        return False, "❌ Insufficient balance."

    bank_balance[payer] -= amount
    bank_balance[payee] += amount

    txn_id = str(uuid.uuid4())[:8]
    txn_log.append({
        'id': txn_id,
        'payer': payer,
        'payee': payee,
        'amount': amount
    })

    return True, f"✅ Payment of ₹{amount} to {payee} successful! (Txn ID: {txn_id})"