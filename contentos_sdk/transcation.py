#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from contentos_sdk.cipher import Secp256k1Cipher
from contentos_sdk.grpc_pb2.prototype import transaction_pb2, type_pb2


class Transaction(object):

    def __init__(self):
        self._transaction = transaction_pb2.transaction

    @property
    def operations(self):
        return self._transaction.operations

    @operations.setter
    def operations_setter(self, operations):
        self._transaction.operations = operations

    @property
    def expiration(self):
        return self._transaction.expiration.utc_seconds

    @expiration.setter
    def expiration_setter(self, expiration):
        self._transaction.expiration = type_pb2.time_point_sec(expiration)

    @property
    def ref_block_num(self):
        return self._transaction.ref_block_num

    @property
    def ref_block_prefix(self):
        return self._transaction.ref_block_prefix

    def to_pb2(self):
        return self._transaction

    def from_block_id(self, block_id):
        if len(block_id) >= 12:
            ref_block_num = int.from_bytes(block_id[:8], "little") % 0x800
            ref_block_prefix = int.from_bytes(block_id[8:12], "big")
            self._transaction.ref_block_num = ref_block_num
            self._transaction.ref_block_prefix = ref_block_prefix
        else:
            self._transaction.ref_block_num = 0
            self._transaction.ref_block_prefix = 0

    def from_dynamic_properties(self, dynamic_properties):
        expiration = dynamic_properties.time.utc_seconds + 30
        self.from_block_id(dynamic_properties.head_block_id.hash)
        self._transaction.expiration = type_pb2.time_point_sec(expiration)

    def sign(self, private_key, chain_id):
        if isinstance(private_key, type_pb2.private_key_type):
            private_key = Secp256k1Cipher.get_private_key_from_raw(
                private_key.data
            )
        else:
            private_key = Secp256k1Cipher.get_private_key_from_wif(private_key)
        serialized_transcation = self._transaction.SerializeToString()
        serialized_len = len(serialized_transcation).to_bytes(4, "big")
        sign_transaction = type_pb2.signed_transaction(
            self._transaction,
            private_key.ecdsa_sign(serialized_len + serialized_transcation)
        )
        return sign_transaction
