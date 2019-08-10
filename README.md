# Contentos Python SDK

[![Build Status](https://travis-ci.org/brickgao/cos-python-sdk.svg?branch=master)](https://travis-ci.org/brickgao/cos-python-sdk)

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

## Keystore

Keystore is password encrypted private key that is in text format or in file.

To create an key store object and manage keys:

```python
from contentos_sdk import KeyStore

key_store = KeyStore()
key_store.add_key("account_name_a", "key")
key = key_store.get_key("account_name_a")
account_names = key_store.get_accounts()
key_store.remove_key("account_name_a")
```

To load from file or dump it:

```python
from contentos_sdk import KeyStore

key_store = KeyStore()
key_store.load_from_file("filename", "badpassword")
# do something
key_store.dump_to_file("filename", "mayanotherbadpassword")
```