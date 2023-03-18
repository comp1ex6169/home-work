a = str(input("Enter name: "))
b = float(input("Enter number of hours worked in a week: "))
c = float(input("Enter hourly pay rate: "))
d = float(input("Enter federal tax: "))
e = float(input("Enter state tax: "))
kuy1 = c*b
ft = (d/100)*kuy1
st = (e/100)*kuy1
total = ft+st
kuy2 = kuy1-total
print(a)
print(b)
print(c)
print(kuy1)
print(ft)
print(st)
print(total)
print(kuy2) 