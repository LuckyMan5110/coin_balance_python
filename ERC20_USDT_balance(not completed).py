from web3 import Web3
import json

# Connect to an Ethereum node. Replace 'http://localhost:8545' with your node's URL if it's remote.
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/YZfmMo3qV3PLNl4okf78ic3HV2gr2Bvd'))


# Check if connected to the node
# if not w3.isConnected():
    # raise Exception("Failed to connect to the Ethereum node")

# Replace with your Ethereum wallet address
wallet_address = '0x7cb6113AC2361aE5ba66984Dd6Ca651fEd6B102d'

# USDT ERC20 contract address on Ethereum mainnet
usdt_contract_address = '0xdac17f958d2ee523a2206206994597c13d831ec7'

# ABI (Application Binary Interface) of the USDT ERC20 contract
usdt_abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')

# Instantiate the contract
contract = w3.eth.contract(address=usdt_contract_address, abi=usdt_abi)

# Function to get USDT balance
def get_usdt_balance(wallet_address):
    try:
        # Call the balanceOf function of the USDT contract
        balance = contract.functions.balanceOf(wallet_address).call()
        # USDT has 6 decimals
        balance_in_usdt = balance / 10**6
        return balance_in_usdt
    except Exception as e:
        print(f'Error getting USDT balance: {e}')
        return None

# Fetch the USDT balance
usdt_balance = get_usdt_balance(wallet_address)
if usdt_balance is not None:
    print(f'USDT Balance: {usdt_balance} USDT')
else:
    print('Failed to retrieve balance')