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

total_price = 1 #Nhập BTC hiện tại
plan_list = [
    11600,
    11550,
    11500,
    11450,
    11400
]
plan_list.sort(reverse=False)

split_price = {}

price = total_price
for x in plan_list:
    price = round(price/2, 8)#Làm tròn 8 số thập phân
    split_price[x] = price


split_price = dict(sorted(split_price.items(), reverse=True))

print('BTC hiện có {0} BTC'.format(total_price))

xx = 0
i = 0
for k in split_price:
    i += 1
    print('Vào lệnh lần {0} : Giá {1} -> {2} BTC'.format(i, k, split_price[k]))
    xx += split_price[k]

print('Tổng các lệnh {0} BTC'.format(xx))


exit
