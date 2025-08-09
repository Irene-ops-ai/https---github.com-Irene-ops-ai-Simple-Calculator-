name = "Irene Ouko"
age = 29
is_student = True

#print(name, age)
#print(is_student)

#Building a basic calculator

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

operation = input("Enter the operation(+, -, *, /):")

if operation == "+":
    result = num1 + num2
    #print(f"{num1} + {num2} = {result}")

elif operation == "-":
 result = num1 - num2
# print(f"{num1} - {num2} = {result}")

elif operation == "*":
   result = num1 * num2
   #print(f"{num1} * {num2} = {result}")

elif operation == "/":
 if num2  != 0:
  result = num1/num2
  #print(f"{num1} / {num2} = {result}")

 else:
   #print("Error: cannot divide by zero")


   #List data structure

   ward_4a = ["Bed1: Angela", "Bed2: Joan", "Bed3: Johnson"]

   print(ward_4a)
