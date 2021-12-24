bill = 0

pizza = input("enter s: small pizza, m: medium pizza, l: large pizza:")
pepperoni = input("need pepperoni? yes/no: ")
cheese = input("extra cheese: yes/no: ")

if pizza == "s":
    print("Small pizza")
    bill += 15
    if pepperoni == "yes":
        bill+=2
elif pizza == "m":
    print("medium pizza")
    bill+= 20
    if pepperoni == "yes":
        bill+=3
else:
    print("large pizza")
    bill+= 25
    if pepperoni == "yes":
        bill+=3

if cheese == "yes":
    bill+=1
    
print(bill)
