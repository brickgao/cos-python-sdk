#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self):
        self.bs = AES.block_size

    def _pad(self, buf):
        pad_ch = chr(self.bs - len(buf) % self.bs)
        pad_cnt = self.bs - len(buf) % self.bs
        return buf + pad_ch * pad_cnt

    def _unpad(self, buf):
        return buf[0:-ord(buf[-1])]

    def encrypt(self, key, buf):
        buf = self._pad(buf)
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(buf).encode("hex")

    def decrypt(self, key, buf):
        cipher = AES.new(key, AES.MODE_ECB)
        return self._unpad(cipher.decrypt(buf))
