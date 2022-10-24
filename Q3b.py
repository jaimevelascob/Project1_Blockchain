from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q3a import (Q3a_txout_scriptPubKey, cust1_private_key, cust2_private_key,
                  cust3_private_key)


def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_private_key)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_private_key)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was locked in the
    # multisig transaction created in Exercise 3a.
    return [bank_sig, cust1_sig]
    ######################################################################


def send_from_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                   txin_scriptPubKey, txout_scriptPubKey, network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = multisig_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0009023 - 0.00001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '3b256d18d010aa2a0ae07c65e58aee0b43ca34ad5d0532fe2698ce2dff42c20a')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = Q3a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_multisig_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)

# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "7483f7a2c992c90b0c430d51ebef50c30aaefa4de14b8bd29c6830fb93bb0248",
#     "addresses": [
#       "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
#     ],
#     "total": 89230,
#     "fees": 1000,
#     "size": 230,
#     "vsize": 230,
#     "preference": "low",
#     "relayed_by": "2a02:2e02:38f0:8600:e6b5:6f51:4383:bc36",
#     "received": "2022-10-24T10:18:44.978211453Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "3b256d18d010aa2a0ae07c65e58aee0b43ca34ad5d0532fe2698ce2dff42c20a",
#         "output_index": 0,
#         "script": "473044022078a6dc881ad7bbbf6a69581708ac82e47ff4dd46af1e0db1087388f80e58eb38022010d05c508457825a5b8d4f4cba5213256b2a8b5c9e0eeaf1342dec33994385e401483045022100ad5e42ba9c720f4eb20857409ebfa75836c46a452dfa53d14fd4b5a8daecb37002202fd15f16bfb261e9c23b342fa3d110805851a5dcdd2d196590d4927db878568501",
#         "output_value": 90230,
#         "sequence": 4294967295,
#         "script_type": "empty",
#         "age": 0
#       }
#     ],
#     "outputs": [
#       {
#         "value": 89230,
#         "script": "76a9149f9a7abd600c0caa03983a77c8c3df8e062cb2fa88ac",
#         "addresses": [
#           "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       }
#     ]
#   }
# }

