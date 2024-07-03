from tronpy import Tron

# Initialize Tron instance
client = Tron()

# Replace with your TRON wallet address
address = 'TNqZ2qx5PCDo5UwpsJTuJTErBmjunf32Hq'
# address = 'TWcPhpvTLkJkUwiQGxm6eMgrYs8oaVqNMT'

# Function to get the TRX balance
def get_trx_balance(address):
    try:
        balance = client.get_account_balance(address)
        return balance
    except Exception as e:
        print(f"Error getting TRX balance: {e}")
        return None

trx_balance = get_trx_balance(address)
if trx_balance is not None:
    print(f'TRX Balance: {trx_balance} TRX')