#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contentos_sdk.grpc_pb2 import grpc_pb2
from contentos_sdk.grpc_pb2.prototype import multi_id_pb2, type_pb2


class Account(object):

    def __init__(self, stub, chain_name, chain_id, key):
        self.stub = stub
        self.chain_nam, self.chain_id = chain_name, chain_id
        self.key = key

    def broadcast_trx(self, signed_trx, wait_result):
        request = grpc_pb2.BroadcastTrxRequest(transaction=signed_trx,
                                               only_deliver=not wait_result)
        return self.stub.BroadcastTrx(request)

    def sign_and_broadcast_trx(self, trx, wait_result):
        dynamic_props = self.get_chain_state().state.dgpo
        trx.from_dynamic_properties(dynamic_props)
        return self.broadcast_trx(trx.sign(self.key, self.chain_id),
                                  wait_result)

    def filter_result(self, trx):
        return self.sign_and_broadcast_trx(trx, True)

    def query_table_content(self, owner, contract, table,
                            field, begin, count, reverse):
        request = grpc_pb2.GetTableContentRequest(owner=owner,
                                                  contract=contract,
                                                  table=table,
                                                  field=field,
                                                  begin=begin,
                                                  count=count,
                                                  reverse=reverse)
        return self.stub.GetTableContent(request)

    def get_account_by_name(self, account_name):
        account_name = type_pb2.account_name(value=account_name)
        request = grpc_pb2.GetAccountByNameRequest(account_name=account_name)
        return self.stub.GetAccountByName(request)

    def get_follower_list_by_name(self, account_name, start_ts,
                                  end_ts, limit, last_order=None):
        start = multi_id_pb2.follower_created_order(
            account=type_pb2.account_name(value=account_name),
            created_time=type_pb2.time_point_sec(utc_seconds=start_ts),
            follower=type_pb2.account_name(value="")
        )
        end = multi_id_pb2.follower_created_order(
            account=type_pb2.account_name(value=account_name),
            created_time=type_pb2.time_point_sec(utc_seconds=end_ts),
            follower=type_pb2.account_name(value="")
        )
        if last_order is None:
            last_order = multi_id_pb2.follower_created_order()
        request = grpc_pb2.GetFollowerListByNameRequest(
            start=start, end=end, limit=limit, last_order=last_order
        )
        return self.stub.GetFollowerListByName(request)

    def get_following_list_by_name(self, account_name, start_ts,
                                   end_ts, limit, last_order=None):
        start = multi_id_pb2.following_created_order(
            account=type_pb2.account_name(value=account_name),
            created_time=type_pb2.time_point_sec(utc_seconds=start_ts),
            follower=type_pb2.account_name(value="")
        )
        end = multi_id_pb2.following_created_order(
            account=type_pb2.account_name(value=account_name),
            created_time=type_pb2.time_point_sec(utc_seconds=end_ts),
            follower=type_pb2.account_name(value="")
        )
        if last_order is None:
            last_order = multi_id_pb2.following_created_order()
        request = grpc_pb2.GetFollowingListByNameRequest(
            start=start, end=end, limit=limit, last_order=last_order
        )
        return self.stub.GetFollowingListByName(request)

    def get_follow_count_by_name(self, account_name):
        account_name = type_pb2.account_name(value=account_name)
        request = grpc_pb2.GetFollowCountByNameRequest(
            account_name=account_name
        )
        return self.stub.GetFollowCountByName(request)

    def get_block_producer_list(self, account_name_start="",
                                limit=10000):
        start = type_pb2.account_name(value="")
        request = grpc_pb2.GetBlockProducerListRequest(
            start=start, limit=limit
        )
        return self.stub.GetBlockProducerList(request)

    def get_block_producer_list_by_vote_count(self, start=None, end=None,
                                              last_block_producer=None,
                                              limit=10000):
        request = grpc_pb2.GetBlockProducerListByVoteCountRequest(
            limit=limit
        )
        if last_block_producer is not None:
            request.last_block_producer.CopyFrom(last_block_producer)
        if start is not None:
            request.start.CopyFrom(type_pb2.vest(value=start))
        if end is not None:
            request.end.CopyFrom(type_pb2.vest(value=end))
        return self.stub.GetBlockProducerListByVoteCount(request)

    def get_post_list_by_created(self, start_ts, end_ts, limit):
        start_ts = type_pb2.time_point_sec(utc_seconds=start_ts)
        start_ts = multi_id_pb2.post_created_order(created=start_ts,
                                                   parent_id=0)
        end_ts = type_pb2.time_point_sec(utc_seconds=end_ts)
        end_ts = multi_id_pb2.post_created_order(created=end_ts,
                                                 parent_id=0)
        request = grpc_pb2.GetPostListByCreatedRequest(start=start_ts,
                                                       end=end_ts,
                                                       limit=limit)
        return self.stub.GetPostListByCreated(request)

    def get_reply_list_by_post_id(self, parent_id, start_ts, end_ts, limit):
        start_ts = type_pb2.time_point_sec(utc_seconds=start_ts)
        start_ts = multi_id_pb2.post_created_order(created=start_ts,
                                                   parent_id=parent_id)
        end_ts = type_pb2.time_point_sec(utc_seconds=end_ts)
        end_ts = multi_id_pb2.post_created_order(created=end_ts,
                                                 parent_id=parent_id)
        request = grpc_pb2.GetReplyListByPostIdRequest(start=start_ts,
                                                       end=end_ts,
                                                       limit=limit)
        return self.stub.GetReplyListByPostId(request)

    def get_chain_state(self):
        request = grpc_pb2.NonParamsRequest()
        return self.stub.GetChainState(request)

    def get_signed_block(self, start):
        request = grpc_pb2.GetSignedBlockRequest(start=start)
        return self.stub.GetSignedBlock(request)

    def get_block_list(self, start, end, limit):
        request = grpc_pb2.GetBlockListRequest(start=start,
                                               end=end,
                                               limit=limit)
        return self.stub.GetBlockList(request)
