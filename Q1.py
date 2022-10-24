from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [signature,public_key]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0010023 - 0.00001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '6de3b04bb3364008276400c5b12c9c8b458608b0132b61b4afed7205085bc576')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)

# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "ee26d853d69c95926fb7fdaf1aebb68b81bf3e2a859c29e850ca1c5208d2f545",
#     "addresses": [
#       "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi",
#       "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
#     ],
#     "total": 99230,
#     "fees": 1000,
#     "size": 191,
#     "vsize": 191,
#     "preference": "low",
#     "relayed_by": "2a02:2e02:38f0:8600:e6b5:6f51:4383:bc36",
#     "received": "2022-10-24T09:40:59.106226227Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "6de3b04bb3364008276400c5b12c9c8b458608b0132b61b4afed7205085bc576",
#         "output_index": 1,
#         "script": "47304402207959027566059bdc097ba58e5c250d9c20c7ce15094a8d181e5291f215886ef4022073bbdd8984a5b784a828173d64f1295abb3264ba0ceeb4e3eeaa06f23b7bb5f5012102ea5b7c135f1e3350e1ea1bbcc283da2de23bf597b9e4617e964ea71bf3bdea39",
#         "output_value": 100230,
#         "sequence": 4294967295,
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash",
#         "age": 0
#       }
#     ],
#     "outputs": [
#       {
#         "value": 99230,
#         "script": "76a9149f9a7abd600c0caa03983a77c8c3df8e062cb2fa88ac",
#         "addresses": [
#           "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       }
#     ]
#   }
# }

