while True:
  i = int(input("Enter number: "))
  if i == 0:
     print("stop")
     break 
  if i%2 == 0:
    print("even")
  elif i%2 != 0:
    print("odd")
  else:
    (" not valid")