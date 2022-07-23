# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:27:28 2022

@author: macwr
"""
from etherscan import Etherscan

eth = Etherscan("WPGM115YX5WX45X4R2V2B42RNRHZKY1RWK")

#save get_gas_oracle() to variable gas_oracle
gas_oracle = eth.get_gas_oracle()

#save SafeGasPrice dictrionary item to variable safe_gas
safe_gas = gas_oracle["SafeGasPrice"]
proposed_gas = gas_oracle["ProposeGasPrice"]
fast_gas = gas_oracle["FastGasPrice"] 

#variable safe_message eqals "Safe:" + safe_gas
safe_message = "Safe: " + safe_gas
proposed_message = "Proposed: " + proposed_gas
fast_message = "Fast: " + fast_gas
L = [safe_message, proposed_message, fast_message]
for i in L:
    print(i)
    
