print("It's a Game of Guess Number")
realNo= 27
count= 0
chances= 5
print("Enter a number To guess: ")
while count<chances:
  count+=1
  guessNo= int(input())
  if guessNo<realNo:
    print("You Entered Low no. Increase it.")
  elif guessNo>realNo:
    print("You Entered High no. Decrease it.")
  elif guessNo==realNo:
    print("Congratulations You Win...")
    print("You Take " + str(count) + " Chances, out of " + str(chances))
    break
  if count==chances:
    print("You Lose")
    print("You Take " + str(count) + " Chances, out of " + str(chances))
    break
  print("You Take " + str(count) + " Chances, out of " + str(chances))
  