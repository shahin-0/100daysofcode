import random

x = input("enter names seperated by commas: ")
names = x.split(",")
y = len(names) -1

n = random.randint(0,y)
print(f"{names[n]} will pay the bill")