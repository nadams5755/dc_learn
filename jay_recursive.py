import sys
sys.setrecursionlimit(10000)

def jay(counter):
  print "counter: " + str(counter)

  print "You're showing Jay snippets of code!"
  print "Do you think He's impressed yet??"

  #answer = raw_input("Type yes or no and hit 'Enter'.").lower()

  # fun
  answer = "foo"

  if answer == "yes" or answer == "y":
    print "you're wrong, he thinks you're a lowlife!"
  elif answer == "no" or answer == "n":
    print "You know your Jay!"
  else:
    print "You didn't pick yes or no! Try again."
    counter = counter + 1
    jay(counter)

jay(0)
