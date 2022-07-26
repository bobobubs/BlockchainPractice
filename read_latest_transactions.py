# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 02:08:56 2022

@author: macwr
"""
import time
import timeit
import pandas
from web3 import Web3
web3 = Web3(Web3.HTTPProvider(
    'https://mainnet.infura.io/v3/f372373ccf164636a2fc76516f4931cb'))

# reads in the data for the most rcent block
def read_single_block():
    block_number = web3.eth.blockNumber
    block = web3.eth.get_block(block_number - 1)
    return block

# reads in the data for the 5 most recent blocks


def read_latest__few_blocks():
    recent_block_number = web3.eth.blockNumber
    for i in range(recent_block_number - 3, recent_block_number + 1):
        block = web3.eth.get_block(i)
        transactions = block['transactions']
        print(transactions)


def parse_transaction(transaction):
    data = web3.eth.get_transaction(transaction)
    return {'tx': data['from'], 'rx': data['to'], 'value': data['value']}


if __name__ == '__main__':
    columns = ['Transmitter', 'Reciever', 'Value']
    df = pandas.DataFrame(columns=columns)
    block = read_single_block()
    print(df)
    while(1):
        try:
            # check to see if the block has changed
            if block['number'] == read_single_block()['number']:
                continue
            else:
                start = timeit.default_timer()
                block = read_single_block()
                transactions = block['transactions']

                for transaction in transactions:
                    try:
                        data = parse_transaction(transaction)
                        df = df.append({'Transmitter': data['tx'],
                                        'Reciever': data['rx'],
                                        'Value': data['value']}, ignore_index=True)
                    except KeyboardInterrupt:
                        print('interrupted')
                        print(df)
                        break
                    except:
                        continue
                stop = timeit.default_timer()

                print('Block ', block['number'], ' parse time: ', stop - start)
        except KeyboardInterrupt:
            print('interrupted')
            print(df)
            break
