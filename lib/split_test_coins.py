from bitcoin import SelectParams
from bitcoin.core import CMutableTransaction, x
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from config import (my_private_key, my_public_key, my_address,
    faucet_address, network_type)

from utils import create_txin, create_txout, broadcast_transaction



def split_coins(amount_to_send, txid_to_spend, utxo_index, n, network):
    txin_scriptPubKey = address.to_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txout_scriptPubKey = address.to_scriptPubKey()
    txout = create_txout(amount_to_send / n, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout]*n)
    sighash = SignatureHash(txin_scriptPubKey, tx,
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx, network)
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    SelectParams('testnet')

    ######################################################################
    # TODO: set these parameters correctly
    private_key = my_private_key
    public_key = private_key.pub
    address = P2PKHBitcoinAddress.from_pubkey(public_key)

    amount_to_send = 0.01032305 - 0.0003 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('4cf3c2e76fb104e0e8aa07bb142ab1721b563a97336dff109324a1b0fc58855e')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    n = 10 # number of outputs to split the input into
    # For n, choose a number larger than what you immediately need, 
    # in case you make mistakes.
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n, network_type)

#     201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "6de3b04bb3364008276400c5b12c9c8b458608b0132b61b4afed7205085bc576",
#     "addresses": [
#       "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#     ],
#     "total": 1002300,
#     "fees": 30005,
#     "size": 498,
#     "vsize": 498,
#     "preference": "low",
#     "relayed_by": "2a02:2e02:38f0:8600:e6b5:6f51:4383:bc36",
#     "received": "2022-10-24T09:38:46.167312342Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 10,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "4cf3c2e76fb104e0e8aa07bb142ab1721b563a97336dff109324a1b0fc58855e",
#         "output_index": 0,
#         "script": "483045022100eeb82d52516213a095b711ed3ede23e32a89714191fe43584308e231833fe4b8022025a86c6ce89f545c11ef31e1c094228e6ff222ecf917067257fad8ee3fb6a7a5012102ea5b7c135f1e3350e1ea1bbcc283da2de23bf597b9e4617e964ea71bf3bdea39",
#         "output_value": 1032305,
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
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 100230,
#         "script": "76a9140b5588757f2c05c487bfbb1d7d56df9f36ce2b3488ac",
#         "addresses": [
#           "mgYtC6zeZY2b1dXCJs1oPYwYUp5tSFQihi"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       }
#     ]
#   }
# }

