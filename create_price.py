#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""
#-----------------------------------------------------------------------------
# Name:        
#
# Purpose:
#
# Version:     1.1
#
# Author:
#
# Created:     06/02/2020
# Updated:     06/02/2020
#
# Copyright:   -
#
#-----------------------------------------------------------------------------
#Check and update outdated packages
#pip install pipupgrade
#pipupgrade --check
#pipupgrade --latest --yes
#
#Export/Import environments
#pip freeze -l > requirements.txt
#pip install -r /path/to/requirements.txt
#-----------------------------------------------------------------------------
"""

split_price_result = {}
define_btc = 1 #Nhập BTC hiện tại
plan_list = [ #Nhập khoảng giá cần vào lệnh
    11600,
    11550,
    11500,
    11450,
    11400,
]

plan_list.sort(reverse=False)

btc = define_btc
total_price = 0
total_btc = 0
for p in plan_list:
    total_price += p
    btc = round(btc/2, 8) #Làm tròn 8 số thập phân
    split_price_result[p] = btc
    total_btc += btc

split_price_result = dict(sorted(split_price_result.items(), reverse=True))

last_btc = split_price_result[list(split_price_result.keys())[-1]]
split_price_result[list(split_price_result.keys())[-1]] = last_btc + (1 - total_btc)

i = 0
total_all_btc = 0
for k in split_price_result:
    i += 1
    print('Vào lệnh lần {0} : Giá {1} USDT -> {2} BTC'.format(i, k, split_price_result[k]))
    total_all_btc += split_price_result[k]

print('BTC hiện có {0} BTC'.format(define_btc))
print('Giá trung bình : {0} USDT'.format(round(total_price/i, 2)))
print('Tổng các lệnh {0} BTC'.format(total_all_btc))
exit
