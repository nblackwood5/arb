#!/bin/env python

#Find arbitrages:
#betting odds
#foreign exhange markets
#cryptocurrrency markets

#forex-
from forex_python.converter import CurrencyRates
c = CurrencyRates()
c.get_rates('USD')

#bitcoin
from forex_python.bitcoin import BtcConverter
b = BtcConverter()
b.get_latest_price('USD')

'''
A
Mcgreggor: +500
Money: -20

B
McG: +400
Money: -25

12.5 McG A -> 62.5
50 Money B -> 62.5
'''