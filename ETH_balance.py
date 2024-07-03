from web3 import Web3

# Connect to a public Ethereum node (e.g., Alchemy, QuickNode, or any other public node provider)
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/YZfmMo3qV3PLNl4okf78ic3HV2gr2Bvd'))

# Replace with your Ethereum wallet address
address = '0x7cb6113AC2361aE5ba66984Dd6Ca651fEd6B102d'

# Function to get ETH balance
def get_eth_balance(address):
    try:
        balance = w3.eth.get_balance(address)
        balance_in_eth = w3.from_wei(balance, 'ether')
        print(f'ETH Balance: {balance_in_eth} ETH')
    except Exception as e:
        print(f'Error getting ETH balance: {e}')

get_eth_balance(address)