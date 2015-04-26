import random
import string

my_bill_dollas = random.randint(0,101)
my_bill_cents = random.randint(0,100)

# insert a zero in the 10s place of the change if it's below $0.10.  ex: $0.04
padding = ""
if my_bill_cents < 10:
  padding = "0"

my_bill = float(str(my_bill_dollas) + "." + padding + str(my_bill_cents))

print "your bill is $" + str(my_bill)

cash_input = str(float(raw_input("how much cash would you like to pay with? ")))

if float(cash_input) < my_bill:
  print "eat shit and wash dishes!"
elif my_bill == float(cash_input):
  print "no change.  get lost shitlord!"
else:
  change = str((float(cash_input) - my_bill)).split('.')

  padding = ""
  if change[1] < 10:
    padding = "0"
  
  print "my change should be $" + str(change[0]) + "." + padding + str(change[1])

  change_d = { 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0 }
  change_c = { 25: 0, 10: 0, 05: 0, 01: 0}

  my_remain_bill = int(change[0])
  for denom in sorted(change_d.keys(), reverse=True):
    if my_remain_bill / denom != 0:
      change_d[denom] = my_remain_bill / denom
      my_remain_bill -= change_d[denom] * denom
  print str(change_d)

  my_remain_coin = int(change[1])
  for denom in sorted(change_c.keys(), reverse=True):
    if my_remain_coin / denom != 0:
      change_c[denom] = my_remain_coin / denom
      my_remain_coin -= change_c[denom] * denom
  print str(change_c)
