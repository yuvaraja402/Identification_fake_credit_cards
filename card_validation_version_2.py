# program modified for creating .exe
# that is executable file

#card 1 example for checking  = 4619 3301 1044 4490
#card 2 example for checking = 4417 1234 5678 9113

from time import *

card_input = input('Enter card digit :')
card_digits = str(card_input)
card = []
for i in card_digits:
    card.append(int(i))
card

i=0
j=1
c=[]
for x in card:
    a=card[i]*2
    b=card[j]
    if a > 9:
        a1=int(a / 10)
        c.append(a1)
        a2 = a % 10
        c.append(a2)
        a=0

    c.append(a)
    c.append(b)
    i=i+2
    j=j+2

    if i>=16:
        break
    if j>=16:
        break
sum_c = sum(c)
if sum_c%10 == 0:
    print("\nCREDIT CARD")
else:
    print("\nNot a CREDIT CARD")

#credit card check over

i=0
j=1
c=[]
for x in card:
    a=card[i]
    b=card[j]*2

    c.append(a)
    c.append(b)
    i=i+2
    j=j+2

    if i>=16:
        break
    if j>=16:
        break
sum_c = sum(c)
if sum_c % 5 == 0:
    print("\nDEBIT CARD")
    print("\nSide Note : Debit card Can be also used in Credit card payment gateway.")
else:
    print("\nNot a DEBIT CARD")

#debit card check over

#checking card type here
if card[0] == 4:
    print("\nTYPE = VISA CARD")
elif card[0] == 5:
    print("\nTYPE = MASTER CARD")
elif card[0] == 6:
    print("\nTYPE = RUPAY / DISCOVER CARD")

sleep(30)
