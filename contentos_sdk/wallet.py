#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import grpc

from contentos_sdk.account import Account
from contentos_sdk.grpc_pb2 import grpc_pb2


class Wallet(object):

    def __init__(self, ip, port):
        self.ip, self.port = ip, port
        self.channel = grpc.insecure_channel(ip + port)
        self.stub = grpc_pb2.ApiService(self.channel)

    def get_account(self, key):
        return Account(self.stub, key)
