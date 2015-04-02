import random
import string

my_bill_dollas = random.randint(0,101)
my_bill_cents = random.randint(0,100)

# insert a 0 in the 10s place of the bill if the change is below $0.10.  ex: $0.04
padding = ""
if my_bill_cents < 10:
  padding = "0"

my_bill = float(str(my_bill_dollas) + "." + padding + str(my_bill_cents))

print "your bill is $" + str(my_bill)

cash_input = str(float(raw_input("how much cash wouldy you like to pay with? ")))

if float(cash_input) < my_bill:
  print "eat shit and wash dishes!"
elif my_bill == float(cash_input):
  print "no change.  get lost shitlord."
else:
  print "change should total " + str((float(cash_input) - my_bill))

  change = str((float(cash_input) - my_bill)).split('.')

  cash = cash_input.split('.')

  my_cash_dollas = int(cash[0])
  my_cash_cents = int(cash[1])

  # cents borrows a dollar if cents are less than the bill's cents.
  if my_cash_cents <  my_bill_cents:
    my_cash_dollas -= 1
    my_cash_cents += 100

  change_d = { '100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '1': 0 }
  change_c = { '25': 0, '10': 0, '5': 0, '1': 0}

  my_remain_bill = int(change[0])
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

  my_remain_coin = int(change[1])

  if my_remain_coin / 25 != 0:
      change_c['25'] = my_remain_coin / 25
      my_remain_coin -= change_c['25'] * 25
  if my_remain_coin / 25 == 0 and my_remain_coin % 25 != 0:
    if my_remain_coin / 10 != 0:
      change_c['10'] = my_remain_coin / 10
      my_remain_coin -= change_c['10'] * 10
  if my_remain_coin / 10 == 0 and my_remain_coin % 10 != 0:
    if my_remain_coin / 5 != 0:
      change_c['5'] = my_remain_coin / 5
      my_remain_coin -= change_c['5'] * 5
  if my_remain_coin / 5 == 0 and my_remain_coin % 5 != 0:
    if my_remain_coin / 1 != 0:
      change_c['1'] = my_remain_coin / 1
      my_remain_coin -= change_c['1'] * 1
  print str(change_c)
