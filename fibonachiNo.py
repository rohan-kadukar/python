# 0,1,1,2,3,5,8,13,.....  ---Fibonachi Numbers
def fib(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  #if n==0 || n==1:
  # return n
  else:
    return fib(n-1)+fib(n-2)

number=int(input("Enter index no. of fibonachi sequence: "))
print(fib(number))