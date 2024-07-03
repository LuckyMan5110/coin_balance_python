from web3 import Web3

# Connect to a BSC node. You can use a public RPC endpoint like Binance's.
bsc = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

# Replace with your BSC address
address = '0xAE7C48bF12C936907B57858147670Ec9243461F3'
# address = '0x8ab10FB8444875b551D6eB3762c015a29b50022A'


# Get the balance
balance_wei = bsc.eth.get_balance(address)

# Convert the balance from wei to BNB
balance_bnb = bsc.from_wei(balance_wei, 'ether')

print(f'Balance: {balance_bnb} BNB')