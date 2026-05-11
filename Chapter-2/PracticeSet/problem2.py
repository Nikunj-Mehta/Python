a = int(input("Enter a number: "))
b = int(input("Enter the divisor: "))

c = a % b # to get the remainder

# print("The remainder when", a ,"is divided by", b ,"is:", c) # comma by default gives a space

# Even simpler and better way of writing is  f"" used for string formatting
print(f"The remainder when {a} is divided by {b} is: {c}")