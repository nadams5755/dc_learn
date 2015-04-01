import random

my_bill_dollas = random.randint(0,101)
my_bill_cents = random.randint(0,100)

my_bill = float(str(my_bill_dollas) + "." + str(my_bill_cents))

print "your bill is $" + str(my_bill)

change_d = { '100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '1': 0 }
change_c = { '25': 0, '10': 0, '5': 0, '1': 0}

my_remain_bill = my_bill_dollas

# integer math, the bill is over $100
if my_remain_bill / 100 != 0:
  change_d['100'] = my_remain_bill / 100 # count bills needed
  my_remain_bill -= change_d['100'] * 100 # update running total
if my_remain_bill / 100 == 0 and my_remain_bill % 100 != 0:
  if my_remain_bill / 50 != 0:
    change_d['50'] = my_remain_bill / 50
    my_remain_bill -= change_d['50'] * 50
if my_remain_bill / 50 == 0 and my_remain_bill % 50 != 0:
  if my_remain_bill / 20 != 0:
    change_d['20'] = my_remain_bill / 20
    my_remain_bill -= change_d['20'] * 20
if my_remain_bill / 20 == 0 and my_remain_bill % 20 != 0:
  if my_remain_bill / 10 != 0:
    change_d['10'] = my_remain_bill / 10
    my_remain_bill -= change_d['10'] * 10
if my_remain_bill / 10 == 0 and my_remain_bill % 10 != 0:
  if my_remain_bill / 5 != 0:
    change_d['5'] = my_remain_bill / 5
    my_remain_bill -= change_d['5'] * 5
if my_remain_bill / 5 == 0 and my_remain_bill % 5 != 0:
  if my_remain_bill / 1 != 0:
    change_d['1'] = my_remain_bill / 1
    my_remain_bill -= change_d['1'] * 1

print str(change_d)
print str(my_remain_bill) + " remain"


