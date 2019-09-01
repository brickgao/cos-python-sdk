#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from contentos_sdk.grpc_pb2.prototype import operation_pb2


class AccountCreate(operation_pb2.account_create_operation):
    pass


class AccountUpdate(operation_pb2.account_update_operation):
    pass


class Transfer(operation_pb2.transfer_operation):
    pass


class TransferToVesting(operation_pb2.transfer_to_vesting_operation):
    pass


class Vote(operation_pb2.vote_operation):
    pass


class BPRegister(operation_pb2.bp_register_operation):
    pass


class BPUnregister(operation_pb2.bp_unregister_operation):
    pass


class BPUpdate(operation_pb2.bp_update_operation):
    pass


class BPVote(operation_pb2.bp_vote_operation):
    pass


class Follow(operation_pb2.follow_operation):
    pass


class ContractDeploy(operation_pb2.contract_deploy_operation):
    pass


class ContractApply(operation_pb2.contract_apply_operation):
    pass


class InternalContractApply(operation_pb2.contract_apply_operation):
    pass


class Post(operation_pb2.post_operation):
    pass


class Reply(operation_pb2.reply_operation):
    pass


class ClaimAll(operation_pb2.claim_all_operation):
    pass


class Report(operation_pb2.report_operation):
    pass


class ConvertVesting(operation_pb2.convert_vesting_operation):
    pass


class Stake(operation_pb2.convert_vesting_operation):
    pass


class Unstake(operation_pb2.un_stake_operation):
    pass
