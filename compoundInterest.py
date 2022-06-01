# a = p(1 + r)

import decimal
from decimal import Decimal

""" amount = 112.31
print(amount)
print(f'{amount:.20f}') """


principal = Decimal('1000.00')
principal
Decimal('1000.00')
rate = Decimal('0.05')
rate
Decimal('0.05')


for year in range(1, 11):
    amount = principal * (1 + rate) ** year 
    print(f'{year:>2}{amount:>10.2f}') 
#Page 100 pdf