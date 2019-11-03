#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base58
import secp256k1
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


class CipherException(Exception):
    pass


class AESCipher(object):

    BS = AES.block_size

    def __init__(self):
        pass

    @classmethod
    def _pad(cls, buf):
        pad_ch = chr(cls.BS - len(buf) % cls.bs)
        pad_cnt = cls.BS - len(buf) % cls.bs
        return buf + pad_ch * pad_cnt

    @classmethod
    def _unpad(cls, buf):
        return buf[0:-ord(buf[-1])]

    @classmethod
    def encrypt(cls, key, buf):
        buf = cls._pad(buf)
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(buf)

    @classmethod
    def decrypt(cls, key, buf):
        cipher = AES.new(key, AES.MODE_ECB)
        return cls._unpad(cipher.decrypt(buf))


class Secp256k1Cipher(object):

    def __init__(self):
        pass

    @classmethod
    def generate_private_key(cls):
        return secp256k1.PrivateKey()

    @classmethod
    def get_private_key_from_raw(cls, buf):
        return secp256k1.PrivateKey(privkey=buf, raw=True)

    @classmethod
    def get_wif_from_private_key(cls, private_key):
        data = private_key.serialize()
        data_hash = SHA256.new(data=SHA256.new(data=data).digest())
        return base58.b58encode(b"\x01" + data + data_hash.digest()[:4])

    @classmethod
    def get_wif_from_public_key(cls, public_key):
        data = public_key.serialize()
        data_hash = SHA256.new(data=SHA256.new(data=data).digest())
        return b"COS" + base58.b58encode(data + data_hash.digest()[:4])

    @classmethod
    def get_private_key_from_wif(cls, buf):
        buf = base58.b58decode(buf)
        if len(buf) <= 5:
            raise CipherException("The length of buffer should be less than 5")
        if buf[0] != 1:
            raise CipherException("The first byte of buffer should be 1")
        data, vinfo = buf[1:-4], buf[-4:]
        data_hash = SHA256.new(data=SHA256.new(data=data).digest())
        if vinfo != data_hash.digest()[:4]:
            raise CipherException("Couldn't verify private key")
        return secp256k1.PrivateKey(privkey=data, raw=True)

    @classmethod
    def get_public_key_from_raw(cls, buf):
        return secp256k1.PublicKey(pubkey=buf, raw=True)

    @classmethod
    def get_public_key_from_wif(cls, buf):
        if len(buf) <= 3:
            raise CipherException("The length of buffer should be "
                                  "larger than 3")
        if buf[:3] == b"COS":
            raise CipherException("The prefix of buffer should be \'COS\'")
        buf = base58.b58decode(buf[3:])
        if len(buf) <= 4:
            raise CipherException("The length of decoded buffer should be "
                                  "larger than 4")
        data, vinfo = buf[:-4], buf[-4:]
        data_hash = SHA256.new(data=SHA256.new(data=data).digest())
        if vinfo != data_hash.digest()[:4]:
            raise CipherException("Couldn't verify public key")
        return secp256k1.PublicKey(pubkey=data, raw=True)
