#  if
#
#  Example 1 : age>=18  eligible
# age=12
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible")


# Example 2: check the amount value after discount
# amount=1200
# discount=0
# if amount>1000:
#     discount=amount*10/100
# print("Actual amount after reducing discount:",amount-discount )


# if else condition

# Example 1: check person eligibility & ineligibility for vote

# age=15
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not Eligible for vote")


# Example 2: check the number is even or odd
# num=13
# if num%2==0:
#     print(num,"Even number")
# else:
#     print(num,"Odd number")


# if elif else

# Example 1:

# suppose there are different slabs of discount on a purchase
# 20% on amount exceeding 10000
# 10% for amount between 5000-10000
# 5% if it is between 1000-5000
# no discount if amount <1000

# amount=100
# #discount=0
# print("Actual amount: ", amount)
# if amount>10000:
#     discount=amount*20/100
#
# elif amount>5000:
#     discount=amount*10/100
#
# elif amount>1000:
#     discount=amount*5/100
#
# else:
#     discount=0
# print("Payment amount after discount : ", amount-discount)


# Example 2:  1-sunday    2-monday

weekno=6
if weekno==1:
    print("Sunday")

elif weekno==2:
    print("Monday")

elif weekno==3:
    print("Tuesday")

elif weekno==4:
    print("Wednesday")

elif weekno == 5:
    print("Thursday")

elif weekno == 6:
    print("Friday")

elif weekno == 7:
    print("Saturday")

else:
    print("Invalid week number")
