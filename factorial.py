def recursiveFactorialForDan(num):
  # base cases for factorials
  if num == 0 or num == 1:
    return 1
  else:
    return num * recursiveFactorialForDan(num-1)

def iterativeFactorialForDan(num):
  # base cases for factorials
  if num == 0 or num == 1:
    return 1
  else:
    result = 1
    # for would stop at x < num,
    # so we need num+1 to actually stop at x=num
    for x in range (1, num+1):
      # short hand for result = result * x
      result *= x
    return result

# show 0! to 6!
print "recursive:" 
for x in range (0, 7):
  print str(x) + "! = " + str(recursiveFactorialForDan(x))

print "iterative:" 
for x in range (0, 7):
  print str(x) + "! = " + str(iterativeFactorialForDan(x))
