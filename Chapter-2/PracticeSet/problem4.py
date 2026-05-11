a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))

if(a > b):
  print(f"{a} is greater than {b}")
elif(b > a): 
  print(f"{b} is greater than {a}")
else:
  print(f"Both {a} and {b} are equal")