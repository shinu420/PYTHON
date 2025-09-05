# #1st question
# login = input("Enter login Id: ")
# password = int(input("Enter password: "))
# if password == 123:
#     print("welcome")
# else:
#     print("invalid error")
#     exit()
# price = int(input("Enter price of commodity: "))
# discount = price -(price*10/100)
# if price < 1000:
#     print("Amount to br paid = ",price)
# else:
#     print("yahh! you got 10%  discount")
#     print("Amount to be paid = ",discount)

# #2nd question
# age = int(input("Enter age: "))
# distance = int(input("Enter distance(in km): "))
# base_fare = 50+(10*distance) 
# print(f"base_fare = 50+(10*distance) =",base_fare)
# if   age <18:
#        final_fare = base_fare -(base_fare*20/100)
#        print("junior discount 20%!applied ")
#        print("final fare=" , final_fare)

# elif age > 60: 
#         final_fare = base_fare -(base_fare*30/100)
#         print("senior discount 30%!applied ")
#         print("final fare=" , final_fare)

# else:
#         print("NO DISCOUNT")
#         print("final fare=" , base_fare)

# # 3rd question

# login_ID = input("Enter login id: ")
# password = input("Enter password: ") 
# if password =="a123":
#     print("welcome")

# else:
#     print("invalid password")
#     exit()
# bill = int(input("Enter bill amount: "))
# if bill <1000 :
#     print("NO DISCOUNT!")
# elif 1000<= bill <=5000:
#     Bill =  bill-(bill*10/100)
#     print("eligible for 10% discount!")
#     print("your bill=" ,Bill)
# else:
#     Bill =  bill-(bill*20/100)
#     print("eligible for 20% discount!")
#     print("your bill=" ,Bill)

# festival = input("is thi festival season?(yes/no): ")
# if festival.lower() == "yes" :
#     print(" you got 5% extra discount!")
#     Bill = Bill -(Bill*5/100)
#     print("festival discounted bill=" , Bill)
# elif festival.lower() == "no":
#     print("better luck next time=", Bill)
# else:
#     print("enter (yes/no) only") 
# print("18% GST added")
# final_payable_amount = Bill+(Bill*18/100)
# print(final_payable_amount)


#4th question
while True:
    i = int(input("Enter no. : "))
    if i == 25:
        print(" you got it")
        break
    elif 20<=i<=30:
        print("you are too close")
    elif i>30:
        print("too big")
    elif i<20:
        print("too samll")
    else:
        print("try between (1-50) for great chance")
        break
print("hello")