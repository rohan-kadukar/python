isPrime=False
num=int(input("Enter an Number: "))
if num<=2:
  isPrime=False
elif num==3:
  isPrime=True
else:
  for i in range(2,num-1):
    if num%i==0:
      isPrime=False
      break
    else:
      isPrime=True
if isPrime==True:
  print(f"Number {num} is prime.")
else:
  print(f"Number {num} is not prime.")