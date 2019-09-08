#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contentos_sdk.grpc_pb2 import grpc_pb2, multi_id_pb2, type_pb2


class Account(object):

    def __init__(self, stub, key):
        self.stub, self.key = stub, key

    def broadcast_trx(self, signed_trx, wait_result):
        request = grpc_pb2.BroadcastTrxRequest(signed_trx, not wait_result)
        return self.stub.BroadcastTrx(request)

    def sign_and_broadcast_trx(self, trx, wait_result):
        dynamic_props = self.stub.GetChainState().state.dgpo
        trx.from_dynamic_properties(dynamic_props)
        return self.broadcast_trx(trx.sign(self.key, 0), wait_result)

    def filter_result(self, trx):
        return self.sign_and_broadcast_trx(trx, True)

    def query_table_content(self, owner, contract, table,
                            field, begin, count, reverse):
        request = grpc_pb2.GetTableContentRequest(owner, contract, table,
                                                  field, begin, count, reverse)
        return self.stub.GetTableContent(request)

    def get_account_by_name(self, account_name):
        account_name = type_pb2.account_name(account_name)
        request = grpc_pb2.GetAccountByNameRequest(account_name)
        return self.stub.GetAccountByName(request)

    def get_account_cash_out(self, block_height):
        request = grpc_pb2.GetBlockCashoutRequest(block_height)
        return self.stub.GetBlockCashout(request)

    def get_follower_list_by_name(self, account_name, start_ts,
                                  end_ts, limit, last_order=None):
        start = multi_id_pb2.follower_created_order(
            type_pb2.account_name(account_name),
            type_pb2.time_point_sec(start_ts),
            type_pb2.account_name("")
        )
        end = multi_id_pb2.follower_created_order(
            type_pb2.account_name(account_name),
            type_pb2.time_point_sec(end_ts),
            type_pb2.account_name("")
        )
        if last_order is None:
            last_order = multi_id_pb2.follower_created_order()
        request = grpc_pb2.GetFollowerListByNameRequest(
            start, end, limit, last_order
        )
        return self.stub.GetFollowerListByName(request)

    def get_following_list_by_name(self, account_name, start_ts,
                                   end_ts, limit, last_order=None):
        start = multi_id_pb2.following_created_order(
            type_pb2.account_name(account_name),
            type_pb2.time_point_sec(start_ts),
            type_pb2.account_name("")
        )
        end = multi_id_pb2.following_created_order(
            type_pb2.account_name(account_name),
            type_pb2.time_point_sec(end_ts),
            type_pb2.account_name("")
        )
        if last_order is None:
            last_order = multi_id_pb2.following_created_order()
        request = grpc_pb2.GetFollowingListByNameRequest(
            start, end, limit, last_order
        )
        return self.stub.GetFollowingListByName(request)

    def get_follow_count_by_name(self, account_name):
        account_name = type_pb2.account_name(account_name)
        request = grpc_pb2.GetFollowCountByNameRequest(account_name)
        return self.stub.GetFollowCountByName(request)

    def get_witness_list(self):
        account_name = type_pb2.account_name("")
        request = grpc_pb2.GetWitnessListRequest(account_name, 1000000)
        return self.stub.GetWitnessList(request)

    def get_post_list_by_created(self, start_ts, end_ts, limit):
        start_ts = type_pb2.time_point_sec(start_ts)
        start_ts = multi_id_pb2.post_created_order(start_ts, 0)
        end_ts = type_pb2.time_point_sec(end_ts)
        end_ts = multi_id_pb2.post_created_order(end_ts, 0)
        request = grpc_pb2.GetPostListByCreatedRequest(start_ts, end_ts, limit)
        return self.stub.GetPostListByCreated(request)

    def get_reply_list_by_post_id(self, parent_id, start_ts, end_ts, limit):
        start_ts = type_pb2.time_point_sec(start_ts)
        start_ts = multi_id_pb2.post_created_order(start_ts, parent_id)
        end_ts = type_pb2.time_point_sec(end_ts)
        end_ts = multi_id_pb2.post_created_order(end_ts, parent_id)
        request = grpc_pb2.GetReplyListByPostIdRequest(start_ts, end_ts, limit)
        return self.stub.GetReplyListByPostId(request)

    def get_chain_state(self):
        request = grpc_pb2.NonParamsRequest()
        return self.stub.GetChainState(request)

    def get_signed_block(self, start):
        request = grpc_pb2.GetSignedBlockRequest(start)
        return self.stub.GetSignedBlock(request)

    def get_block_list(self, start, end, limit):
        request = grpc_pb2.GetBlockListRequest(start, end, limit)
        return self.stub.GetBlockList(request)
