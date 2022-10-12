num1= float(input("Enter First Number: "))
num2= float(input("Enter Second Number: "))
print("Please Select The Operator\n"
              "a. Addition\n"
              "b. Substraction\n"
              "c. Multiplication\n"
              "d. Division")
oper= input("Please Select Your Operator: ")

if oper== 'a':
  print(num1," + ",num2," is ", num1+num2)
elif oper== 'b':
  print(num1," - ",num2," is ", num1-num2)
elif oper== 'c':
  print(num1," * ",num2," is ", num1*num2)
elif oper== 'd':
  print(num1," / ",num2," is ", num1/num2)
else:
  print("Invalid Choice")