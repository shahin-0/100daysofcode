yname = input("enter your name")
cname = input("enter your crush's name")


x = yname + cname
val = x.lower()

t = val.count("t")
r = val.count("R")
u = val.count("u")
e = val.count("e")
l = val.count("l")
o = val.count("o")
v = val.count("v")

c = (t + r + u + e + l + o +v)/7 * 100
print(c)