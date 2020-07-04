#!/usr/bin/env python
# coding: utf-8

from time import *

digits = input('Enter card number : ')
card=[]
for i in digits:
    card.append(i)

# Credit Card check
i=0
j=1
odd=[]
even=[]
for x in card:
    odd.append(card[i])
    even.append(card[j])
    i+=2
    j+=2
    if i >= 16:
        break

odd = list(map(int,odd))
even = list(map(int,even))
odd = [x * 2 for x in odd]

for i in range(len(odd)):
    if odd[i] > 9:
        modulus = int(odd[i]%10)
        divisor = int(odd[i]/10)
        odd[i]=modulus+divisor

if (sum(odd)+sum(even))%10 == 0:
    print('\nValid Credit Card\n')
else:
    print('\nInvalid Credit Card\n')
    

# Checking payment network
discover = ['6011','644','645','646','647','648','649','622126','622925']
payment = ['American express','MasterCard','RuPay','Visa']
prefix = ['3','5','6','4']


for i in range(len(prefix)):
    if digits.startswith(prefix[i]) == True:
        network = payment[i]+' Payment network'

for i in range(len(discover)):
    if digits.startswith(discover[i]) == True:
        network = 'Discover Payment network'
print(network)

sleep(30)