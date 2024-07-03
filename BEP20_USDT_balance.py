from web3 import Web3

# Connect to a BSC node. You can use a public RPC endpoint like Binance's.
bsc = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

# Replace with your BSC address
address = '0xAE7C48bF12C936907B57858147670Ec9243461F3'
# address = '0x8ab10FB8444875b551D6eB3762c015a29b50022A'

# USDT BEP20 contract address on BSC
contract_address = '0x55d398326f99059fF775485246999027B3197955'

# ABI of the balanceOf method
abi = [
    {
        "constant": True,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "type": "function"
    }
]

# Create a contract instance
contract = bsc.eth.contract(address=contract_address, abi=abi)

# Function to get the BEP20 USDT balance
def get_usdt_balance(address):
    balance = contract.functions.balanceOf(address).call()
    # Convert the balance from wei (smallest unit) to USDT
    balance_in_usdt = bsc.from_wei(balance, 'ether')
    return balance_in_usdt

usdt_balance = get_usdt_balance(address)
print(f'USDT Balance: {usdt_balance} USDT')