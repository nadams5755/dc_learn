import random

my_bill_dollas = random.randint(0,101)
my_bill_cents = random.randint(0,100)

my_bill = float(str(my_bill_dollas) + "." + str(my_bill_cents))

print "your bill is $" + str(my_bill)

change_d = { '100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '1': 0 }
change_c = { '25': 0, '10': 0, '5': 0, '1': 0}

my_new_bill = 0

if my_new_dollas / 100 != 0:
    change_d['100'] = my_dolla_bills / 100

if my_bill_dollas / 100 == 0 and my_bill_dollas % 100 != 0:
    my_new_bill += my_bill_dollas % 100

