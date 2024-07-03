from tronpy import Tron
# from tronpy.exceptions import TronError

# Initialize Tron instance
client = Tron()

# Replace with your TRON wallet address
address = 'TNqZ2qx5PCDo5UwpsJTuJTErBmjunf32Hq'
# address = 'TWcPhpvTLkJkUwiQGxm6eMgrYs8oaVqNMT'


# USDT TRC20 contract address on Tron
contract_address = 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'

# Function to get the TRC20 USDT balance
def get_usdt_balance(address, contract_address):
    try:
        # Get the contract instance
        contract = client.get_contract(contract_address)

        # Call the balanceOf method of the contract
        balance = contract.functions.balanceOf(address)
        # USDT has 6 decimal places
        balance_in_usdt = balance / 10**6
        return balance_in_usdt
    except Exception as e:
        print(f"Error getting USDT balance: {e}")
        return None

# Fetch the USDT balance
usdt_balance = get_usdt_balance(address, contract_address)
if usdt_balance is not None:
    print(f'USDT Balance: {usdt_balance} USDT')
else:
    print('Failed to retrieve balance')