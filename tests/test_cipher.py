#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii

from contentos_sdk.cipher import AESCipher, Secp256k1Cipher


def test_aes_encrypt_and_decrypt():
    key, data = b'badkeybadkey0123', b'test'
    encrypted_data = AESCipher.encrypt(key, data)
    assert data != encrypted_data
    assert data == AESCipher.decrypt(key, encrypted_data)


def test_secp256k1_generate_private_key():
    privkey = Secp256k1Cipher.generate_private_key()
    assert privkey.serialize() != b""
    assert privkey.pubkey.serialize() != b""


def test_secp256k1_get_private_key_from_raw():
    privkey = Secp256k1Cipher.generate_private_key()
    privkey2 = Secp256k1Cipher.get_private_key_from_raw(
        binascii.unhexlify(privkey.serialize())
    )
    assert privkey.serialize() == privkey2.serialize()


def test_secp256k1_get_public_key_from_raw():
    privkey = Secp256k1Cipher.generate_private_key()
    pubkey = Secp256k1Cipher.get_public_key_from_raw(
        privkey.pubkey.serialize()
    )
    assert privkey.pubkey.serialize() == pubkey.serialize()


def test_secp256k1_convert_between_private_key_and_wif():
    privkey = Secp256k1Cipher.generate_private_key()
    wif = Secp256k1Cipher.get_wif_from_private_key(privkey)
    privkey2 = Secp256k1Cipher.get_private_key_from_wif(wif)
    assert privkey.serialize() == privkey2.serialize()


def test_secp256k1_convert_between_public_key_and_wif():
    privkey = Secp256k1Cipher.generate_private_key()
    pubkey = privkey.pubkey
    wif = Secp256k1Cipher.get_wif_from_public_key(pubkey)
    pubkey2 = Secp256k1Cipher.get_public_key_from_wif(wif)
    assert pubkey.serialize() == pubkey2.serialize()
