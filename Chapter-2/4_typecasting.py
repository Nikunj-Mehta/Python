a = 31.3
t = type(a)
print(t)

b = "23.2"
i = type(b)
print(i)

c = float(b) # function which converts string to float if valid
j = type(c)
print(j)

d = int(c) # string with float value can't be converted to int directly
k = type(d) # but convert it to float and then it can be converted to int
print(k)