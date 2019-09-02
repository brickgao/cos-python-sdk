#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from Crypto.Hash import SHA256

from contentos_sdk.cipher import AESCipher


class KeyStore(object):

    def __init__(self):
        self.account_to_key = dict()

    def get_key(self, account):
        return self.account_to_key[account]

    def add_key(self, account, key):
        self.account_to_key[account] = key

    def remove_key(self, account):
        self.account_to_key.pop(account)

    def get_accounts(self):
        return self.account_to_key.keys()

    def load_from_file(self, filename, password):
        secret_key = SHA256.new().update(password).digest()
        with open(filename, "rb") as f:
            buf = f.read()
        json_data = AESCipher.decrypt(secret_key, buf)
        self.self.account_to_key = json.loads(json_data)

    def dump_to_file(self, filename, password):
        secret_key = SHA256.new().update(password).digest()
        json_data = json.dumps(self.account_to_key)
        buf = AESCipher.encrypt(secret_key, json_data)
        with open(filename, "wb") as f:
            f.write(buf)
