n = int(input("Enter number: " ))

if n%2 != 0 :
    print("weird")
elif n%2 == 0:
    if n<= 5:
        print("not weird")
    elif n>5 and n <= 20 :
        print("weird")
    else:
        print("not weird")
else:
    print("enter valid  number")