# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:47:07 2022

@author: macwr
"""

from etherscan import Etherscan
eth = Etherscan("WPGM115YX5WX45X4R2V2B42RNRHZKY1RWK")
address = "0xda6bde7298acfc730a4f51ad260db9ccc91b1cf3"

#Get the eth balance for a single address
#output is account balance in wei
response = eth.get_eth_balance("0xda6bde7298acfc730a4f51ad260db9ccc91b1cf3") #returns dict
print(response)

#Get the eth balance for up to 20 addresses
#output is dictonary of addresses and balances
addresses = ["0xda6bde7298acfc730a4f51ad260db9ccc91b1cf3", 
             "0x601149d446fd8a2e6f482a7869f0df2589504961",
             "0x6d8b012ea4c3482ebfa49cf9faafdf6fd56bce69"]
response = eth.get_eth_balance_multiple(addresses)
for i in range(len(addresses)):
    print(response[i]['balance'])
