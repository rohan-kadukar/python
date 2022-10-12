num=int(input("Enter an Number: "))
if num<=2:
  print(f"Number {num} is not prime.")
elif num==3:
  print(f"Number {num} is prime.")
else:
  for i in range(2,num-1):
    if num%i==0:
      print(f"Number {num} is not prime.")
      break
  else:
      print(f"Number {num} is prime.")