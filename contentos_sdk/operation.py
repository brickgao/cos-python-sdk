#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from contentos_sdk.grpc_pb2.prototype import (operation_pb2, transaction_pb2,
                                              type_pb2)


class AccountCreate(object):

    def __init__(self, fee, creator, new_account_name,
                 pub_key, json_metadata):
        self.fee = fee
        self.creator, self.new_account_name = creator, new_account_name
        self.pub_key = pub_key
        self.json_metadata = json_metadata
        _operation = operation_pb2.account_create_operation(
            fee=type_pb2.coin(value=fee),
            creator=type_pb2.account_name(value=creator),
            new_account_name=type_pb2.account_name(value=new_account_name),
            pub_key=type_pb2.public_key_type(data=pub_key.serialize()),
            json_metadata=json_metadata
        )
        self.operation = transaction_pb2.operation(op1=_operation)
