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
split_num = 10 #Nhập số lần vào lệnh
split_price = []

price = total_price
for x in range(split_num):
    price = round(price/2, 8)#Làm tròn 8 số thập phân
    split_price.append(price)

split_price.sort()

print('BTC hiện có {0} BTC'.format(total_price))
#print(split_price)

xx = 0
i = 0
for p in split_price:
    i += 1
    print('Giá vào lệnh lần {0} là : {1} BTC'.format(i, p))
    xx += p

print('Tổng các lệnh {0} BTC'.format(xx))


exit
