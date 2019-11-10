#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from contentos_sdk.grpc_pb2.prototype import (operation_pb2, transaction_pb2,
                                              type_pb2)


class ChainProperties(object):

    def __init__(self, account_creation_fee, stamina_free, tps_expected,
                 top_n_acquire_free_token, epoch_duration, per_ticket_price,
                 per_ticket_weight):
        self.account_creation_fee = account_creation_fee
        self.stamina_free = stamina_free
        self.tps_expected = tps_expected
        self.top_n_acquire_free_token = top_n_acquire_free_token
        self.epoch_duration = epoch_duration
        self.per_ticket_price = per_ticket_price
        self.per_ticket_weight = per_ticket_weight

    def to_pb2(self):
        return type_pb2.chain_properties(
            account_creation_fee=type_pb2.coin(
                value=self.account_creation_fee
            ),
            stamina_free=self.stamina_free,
            tps_expected=self.tps_expected,
            top_n_acquire_free_token=self.top_n_acquire_free_token,
            epoch_duration=self.epoch_duration,
            per_ticket_price=type_pb2.coin(
                value=self.per_ticket_price
            ),
            per_ticket_weight=self.per_ticket_weight
        )


class BeneficiaryRouteType(object):

    def __init__(self, name, weight):
        self.name, self.weight = name, weight

    def to_pb2(self):
        return type_pb2.beneficiary_route_type(
            name=self.name, weight=self.weight
        )


class AccountCreateOperation(object):

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


class AccountUpdateOperation(object):

    def __init__(self, owner, pub_key):
        self.owner = owner
        self.pub_key = pub_key
        _operation = operation_pb2.account_update_operation(
            owner=type_pb2.account_name(value=owner),
            pub_key=type_pb2.public_key_type(data=pub_key.serialize())
        )
        self.operation = transaction_pb2.operation(op20=_operation)


class TransferOperation(object):

    def __init__(self, account_from, account_to, amount, memo):
        self.account_from, self.account_to = account_from, account_to
        self.amount, self.memo = amount, memo
        _operation = operation_pb2.transfer_operation(
            to=type_pb2.account_name(value=account_to),
            amount=type_pb2.coin(value=amount),
            memo=memo
        )
        getattr(_operation, "from").CopyFrom(
            type_pb2.account_name(value=account_from)
        )
        self.operation = transaction_pb2.operation(op2=_operation)


class TransferToVestOperation(object):

    def __init__(self, account_from, account_to, amount, memo):
        self.account_from, self.account_to = account_from, account_to
        self.amount, self.memo = amount, memo
        _operation = operation_pb2.transfer_to_vest_operation(
            to=type_pb2.account_name(value=account_to),
            amount=type_pb2.coin(value=amount),
            memo=memo
        )
        getattr(_operation, "from").CopyFrom(
            type_pb2.account_name(value=account_from)
        )
        self.operation = transaction_pb2.operation(op10=_operation)


class VoteOperation(object):

    def __init__(self, voter, idx):
        self.voter, self.idx = voter, idx
        _operation = operation_pb2.vote_operation(
            voter=type_pb2.account_name(value=voter),
            idx=idx
        )
        self.operation = transaction_pb2.operation(op9=_operation)


class BpRegisterOperation(object):

    def __init__(self, owner, url, desc, block_signing_key, props):
        self.owner = owner
        self.url, self.desc = url, desc
        self.block_signing_key = block_signing_key
        self.props = props
        _operation = operation_pb2.bp_register_operation(
            owner=type_pb2.account_name(value=owner),
            url=url,
            desc=desc,
            block_signing_key=type_pb2.public_key_type(
                data=block_signing_key.serialize()
            ),
            props=props.to_pb2()
        )
        self.operation = transaction_pb2.operation(op3=_operation)


class BpUpdateOperation(object):

    def __init__(self, owner, props):
        self.owner = owner
        self.props = props
        _operation = operation_pb2.bp_update_operation(
            owner=type_pb2.account_name(value=owner),
            props=props.to_pb2()
        )
        self.operation = transaction_pb2.operation(op19=_operation)


class BpEnableOperation(object):

    def __init__(self, owner, cancel):
        self.owner = owner
        self.cancal = cancel
        _operation = operation_pb2.bp_enable_operation(
            owner=type_pb2.account_name(value=owner),
            cancel=cancel
        )
        self.operation = transaction_pb2.operation(op4=_operation)


class BpVoteOperation(object):

    def __init__(self, voter, block_producer, cancel):
        self.voter, self.block_producer = voter, block_producer
        self.cancel = cancel
        _operation = operation_pb2.bp_vote_operation(
            voter=type_pb2.account_name(value=voter),
            voblock_producerer=type_pb2.account_name(value=block_producer),
            cancel=cancel
        )
        self.operation = transaction_pb2.operation(op5=_operation)


class FollowOperation(object):

    def __init__(self, account, f_account, cancel):
        self.account, self.f_account = account, f_account
        self.cancel = cancel
        _operation = operation_pb2.follow_operation(
            account=type_pb2.account_name(value=account),
            f_account=type_pb2.account_name(value=f_account),
            cancel=cancel
        )
        self.operation = transaction_pb2.operation(op8=_operation)


class ContractDelayOperation(object):

    def __init__(self, owner, contract, abi, code, upgradeable, url, describe):
        self.owner = owner
        self.contract = contract
        self.abi, self.code = abi, code
        self.upgradeable = upgradeable
        self.url, self.describe = url, describe
        _operation = operation_pb2.contract_deploy_operation(
            owner=type_pb2.account_name(value=owner),
            contract=contract,
            abi=abi, code=code,
            upgradeable=upgradeable,
            url=url, describe=describe
        )
        self.operation = transaction_pb2.operation(op13=_operation)


class ContractApplyOperation(object):

    def __init__(self, caller, owner, contract, method, params, amount):
        self.caller, self.owner = caller, owner
        self.contract = contract
        self.method, self.params = method, params
        self.amount = amount
        _operation = operation_pb2.contract_apply_operation(
            caller=type_pb2.account_name(value=caller),
            owner=type_pb2.account_name(owner=owner),
            contract=contract,
            method=method, params=params,
            amount=type_pb2.coin(value=amount)
        )
        self.operation = transaction_pb2.operation(op14=_operation)


class PostOperation(object):

    def __init__(self, uuid, owner, title, content, tags, beneficiaries):
        self.uuid = uuid
        self.owner = owner
        self.title, self.content = title, content
        self.tags, self.beneficiaries = tags, beneficiaries
        _operation = operation_pb2.post_operation(
            uuid=uuid,
            owner=type_pb2.account_name(owner=owner),
            title=title, content=content,
            tags=tags,
            beneficiaries=list(map(lambda x: x.to_pb2(), beneficiaries))
        )
        self.operation = transaction_pb2.operation(op6=_operation)


class ReplyOperation(object):

    def __init__(self, uuid, owner, content, parent_uuid, beneficiaries):
        self.uuid = uuid
        self.owner = owner
        self.content = content
        self.parent_uuid = parent_uuid
        self.beneficiaries = beneficiaries
        _operation = operation_pb2.reply_operation(
            uuid=uuid,
            owner=type_pb2.account_name(owner=owner),
            content=content,
            parent_uuid=parent_uuid,
            beneficiaries=list(map(lambda x: x.to_pb2(), beneficiaries))
        )
        self.operation = transaction_pb2.operation(op7=_operation)


class ConvertVestOperation(object):

    def __init__(self, account_from, amount):
        self.account_from = account_from
        self.amount = amount
        _operation = operation_pb2.convert_vest_operation(
            amount=type_pb2.vest(value=amount)
        )
        getattr(_operation, "from").CopyFrom(
            type_pb2.account_name(value=account_from)
        )
        self.operation = transaction_pb2.operation(op16=_operation)


class StakeOperation(object):

    def __init__(self, account_from, account_to, amount):
        self.account_from, self.account_to = account_from, account_to
        self.amount = amount
        _operation = operation_pb2.stake_operation(
            to=type_pb2.account_name(value=account_to),
            amount=type_pb2.coin(value=amount),
        )
        getattr(_operation, "from").CopyFrom(
            type_pb2.account_name(value=account_from)
        )
        self.operation = transaction_pb2.operation(op17=_operation)


class UnstakeOperation(object):

    def __init__(self, account_from, account_to, amount):
        self.account_from, self.account_to = account_from, account_to
        self.amount = amount
        _operation = operation_pb2.un_stake_operation(
            to=type_pb2.account_name(value=account_to),
            amount=type_pb2.coin(value=amount),
        )
        getattr(_operation, "from").CopyFrom(
            type_pb2.account_name(value=account_from)
        )
        self.operation = transaction_pb2.operation(op18=_operation)


class AcquireTicketOperation(object):

    def __init__(self, account, count):
        self.account = account
        self.count = count
        _operation = operation_pb2.acquire_ticket_operation(
            account=type_pb2.account_name(value=account),
            count=count
        )
        self.operation = transaction_pb2.operation(op21=_operation)


class VoteByTicketOperation(object):

    def __init__(self, account, idx, count):
        self.account = account
        self.idx = idx
        self.count = count
        _operation = operation_pb2.vote_by_ticket_operation(
            account=type_pb2.account_name(value=account),
            idx=idx,
            count=count
        )
        self.operation = transaction_pb2.operation(op22=_operation)
