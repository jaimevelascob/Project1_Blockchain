from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q2a import Q2a_txout_scriptPubKey

# id = 171
######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0009923 - 0.0001  # amount of BTC in the output you're sending minus fee
txid_to_spend = ('76712f044be084250b9012e205bcaf4db2b0ff37acd658b541f82fcac2faa786')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.
txin_scriptSig = [9,8]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)

# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "197d7eee34c1cd2468dfe53b15464cf9a0a5a07c055889f431c913e578a0b3bc",
#     "addresses": [
#       "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
#     ],
#     "total": 89230,
#     "fees": 10000,
#     "size": 87,
#     "vsize": 87,
#     "preference": "high",
#     "relayed_by": "2a02:2e02:38f0:8600:e6b5:6f51:4383:bc36",
#     "received": "2022-10-24T10:02:34.324593761Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "76712f044be084250b9012e205bcaf4db2b0ff37acd658b541f82fcac2faa786",
#         "output_index": 0,
#         "script": "5958",
#         "output_value": 99230,
#         "sequence": 4294967295,
#         "script_type": "unknown",
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

