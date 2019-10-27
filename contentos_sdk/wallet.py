#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zlib

import grpc

from contentos_sdk.account import Account
from contentos_sdk.grpc_pb2 import grpc_pb2_grpc


class Wallet(object):

    def __init__(self, chain_name, ip, port):
        self.chain_name = chain_name
        self.chain_id = zlib.crc32(chain_name.encode("ascii"))
        self.ip, self.port = ip, port
        self.channel = grpc.insecure_channel(ip + ":" + str(port))
        self.stub = grpc_pb2_grpc.ApiServiceStub(self.channel)

    def get_account(self, key):
        return Account(self.stub, self.chain_name, self.chain_id, key)
