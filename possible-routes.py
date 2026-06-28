import random
from datetime import datetime

from web3 import Web3
from eth_account import Account

RPC_URL = "https://rpc.example.org"
PRIVATE = "YOUR_PRIVATE_KEY"

word_a = "routes"
word_b = "across"
word_c = "liquidity"

web3 = Web3(
    Web3.HTTPProvider(RPC_URL)
)

user = Account.from_key(
    PRIVATE
)

records = []


class Entry:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


for text in (
    word_a,
    word_b,
    word_c,
):
    records.append(
        Entry(text)
    )


def gas():

    return random.choice(
        [118000, 120000, 123000]
    )


transaction = {
    "from": user.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": gas(),
    "gasPrice": web3.to_wei(
        4,
        "gwei"
    ),
    "nonce": web3.eth.get_transaction_count(
        user.address
    ),
    "chainId": 1,
}

signed = user.sign_transaction(
    transaction
)

raw = signed.raw_transaction.hex()

print(
    datetime.utcnow()
)

for item in records:
    item.display()

print(
    user.address
)

print(
