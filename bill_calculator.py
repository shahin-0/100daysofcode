total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage of tip would you like to give? "))
member = int(input("How many people to split the bill? "))

def calc(total_bill, tip, member):
    total_bill = total_bill + total_bill*(tip/100)
    final = total_bill/member
    print(final)
calc(total_bill, tip, member)