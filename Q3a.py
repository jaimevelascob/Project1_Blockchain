from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cSVixZDH7WV7AU8UDf6NY3bdiuT7WhiskJNSK76mfh4xsdxXj57r')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cW2r3n2L5V3cPZWtYPTd4H2zmDeS3fBdjgaWbrJbqNk1dYwabNvu')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cQh1m9PCRmx4DMcDco4xFmvovxogbCStbMX2yySwN9Ymu5ojenpe')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
        # fill this in!
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0010023 - 0.0001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '6de3b04bb3364008276400c5b12c9c8b458608b0132b61b4afed7205085bc576')
    utxo_index = 3 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "3b256d18d010aa2a0ae07c65e58aee0b43ca34ad5d0532fe2698ce2dff42c20a",
#     "addresses": [
#       "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#     ],
#     "total": 90230,
#     "fees": 10000,
#     "size": 166,
#     "vsize": 166,
#     "preference": "low",
#     "relayed_by": "2a02:2e02:38f0:8600:e6b5:6f51:4383:bc36",
#     "received": "2022-10-24T10:11:32.941001637Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "6de3b04bb3364008276400c5b12c9c8b458608b0132b61b4afed7205085bc576",
#         "output_index": 3,
#         "script": "47304402204a9390aad222e71c9b01f592cd2f3909f652f38c589b8b671d103e8fc97e89fc0220467e59ef67699e9f8165bf991d56b36c456c3d0f29f9eb7f2188a03a4f6abcd8012102ea5b7c135f1e3350e1ea1bbcc283da2de23bf597b9e4617e964ea71bf3bdea39",
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
#         "value": 90230,
#         "addresses": null,
#         "script_type": "empty"
#       }
#     ]
#   }
# }

