#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contentos_sdk.key_store import KeyStore


def test_key_store():
    key_store = KeyStore()
    key_store.add_key("account1", "key1")
    key_store.add_key("account2", "key2")
    assert key_store.get_key("account1") == "key1"
    assert key_store.get_accounts() == ["account1", "account2"]

    key_store.remove_key("account2")
    assert key_store.get_accounts() == ["account1"]

    key_store2 = KeyStore()
    key_store.dump_to_file("dummy", b"badpasswd")
    key_store2.load_from_file("dummy", b"badpasswd")
    assert key_store2.get_accounts() == key_store.get_accounts()
