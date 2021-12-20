age = int(input("whats your current age? "))

def calc(age, target):
    days = target*365 - age*365
    months = target*12 - age*12
    weeks = target*52.143 - age*52
    return f"you have {days} days, {months} months and {weeks}weeks left"
    
print(calc(age, 90))