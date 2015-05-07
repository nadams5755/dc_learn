mytest = str(raw_input("test for palindrome: "));

peer_char = len(mytest) - 1
palindrome = False

for ch in mytest:
  if peer_char >= (len(mytest))/2:
    if ch == mytest[peer_char]:
      print "letters match " + ch + ":" + mytest[peer_char]
      peer_char -= 1
      palindrome = True
    else:
      print "letters don't match " + ch + ":" + mytest[peer_char]
      palindrome = False
      break
  else:
    break

if palindrome == True:
  print "it's a palindrome."
else:
  print "not a palindrome."
