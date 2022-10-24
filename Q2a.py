from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [OP_2DUP, OP_ADD, 17, OP_EQUALVERIFY, OP_SUB, 1 , OP_EQUAL]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0010023 - 0.00001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '6de3b04bb3364008276400c5b12c9c8b458608b0132b61b4afed7205085bc576')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "76712f044be084250b9012e205bcaf4db2b0ff37acd658b541f82fcac2faa786",
#     "addresses": [
#       "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#     ],
#     "total": 99230,
#     "fees": 1000,
#     "size": 175,
#     "vsize": 175,
#     "preference": "low",
#     "relayed_by": "2a02:2e02:38f0:8600:e6b5:6f51:4383:bc36",
#     "received": "2022-10-24T10:01:46.212732235Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "6de3b04bb3364008276400c5b12c9c8b458608b0132b61b4afed7205085bc576",
#         "output_index": 2,
#         "script": "483045022100e8214573a55447a6694148b2372e645228a401ef9577b22ef36871a4bbe9008a022067ea1e8d521c52edc35efcbc669eb34302b2c933b93bb48782533cb3143bb881012102ea5b7c135f1e3350e1ea1bbcc283da2de23bf597b9e4617e964ea71bf3bdea39",
#         "output_value": 100230,
#         "sequence": 4294967295,
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash",
#         "age": 2377967
#       }
#     ],
#     "outputs": [
#       {
#         "value": 99230,
#         "script": "6e93011188945187",
#         "addresses": null,
#         "script_type": "unknown"
#       }
#     ]
#   }
# }
