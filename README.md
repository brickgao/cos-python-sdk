# Contentos Python SDK

[![Build Status](https://travis-ci.org/brickgao/cos-python-sdk.svg?branch=master)](https://travis-ci.org/brickgao/cos-python-sdk) [![Coverage Status](https://coveralls.io/repos/github/brickgao/cos-python-sdk/badge.svg?branch=master)](https://coveralls.io/github/brickgao/cos-python-sdk?branch=master)

**Notice: it's still under development**

Python library of the client for Contentos blockchain.

## Installation

To install, simply use pip:

```shell
$ pip install contentos_sdk
```

Or you could clone the repository and install by hand:

```shell
$ git clone https://github.com/brickgao/cos-python-sdk.git
$ cd cos-python-sdk
$ python setup.py install
```

## Quick start

### Keystore

Keystore is password encrypted private key that is in text format or in file.

To create an key store object and manage keys:

```python
from contentos_sdk.key_store import KeyStore


key_store = KeyStore()
key_store.add_key("account_name_a", "key")
key = key_store.get_key("account_name_a")
account_names = key_store.get_accounts()
key_store.remove_key("account_name_a")
```

To load from file or dump it:

```python
from contentos_sdk.key_store import KeyStore


key_store = KeyStore()
key_store.load_from_file("filename", "badpassword")
# do something
key_store.dump_to_file("filename", "badpassword")
```

### Wallet

Wallet provides the way to specific the entry of API and chain ID, and you could get accounts from the wallet.

To set up a wallet and get a account from it:

```python
from contentos_sdk.wallet import Wallet


wallet = contentos_sdk.Wallet("test", "localhost", 8888)
account = wallet.get_account("4DjYx2KAGh1NP3dai7MZTLUBMMhMBPmwouKE8jhVSESywccpVZ")
```

### Account

With private key, account provides the way to access the chain, e.g.: 

```python
# Get the information of account by account name
rsp = account.get_account_by_name("initminer")
# Get the state of chain
rsp = account.get_chain_state()
```

### Transcation

The transcation hold your operations to the blockchain.

To let it take effect, you must broadcast it with your account. e.g.

```python
from contentos_sdk.cipher import Secp256k1Cipher
from contentos_sdk.transcation import Transaction
from contentos_sdk.operation import AccountCreateOperation, TransferOperation

# Create a new account
trx = Transaction()
privkey = Secp256k1Cipher.generate_private_key()
op = AccountCreateOperation(
    fee=1000000,
    creator="initminer",
    new_account_name="testuser007",
    pub_key=privkey.pubkey,
    json_metadata=""
)
trx.operations = [op]
rsp = account.sign_and_broadcast_trx(trx, True)


# Make a transfer
trx = Transaction()
op = TransferOperation(
    account_from="initminer",
    account_to="testuser007",
    amount=1000,
    memo="test_memo"
)
trx.operations = [op]
rsp = account.sign_and_broadcast_trx(trx, True)
```

## License

MIT