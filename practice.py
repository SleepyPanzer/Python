import random
Num_1= int(input("enter lower bound  :"))
Num_2= int(input("enter upper bound  :"))
answer =random.randrange(Num_1,Num_2)
print("Lets start the game ")
totalguess=7
count=0
while count <totalguess:
  count+=1
  guess=int(input("guess the number "))
  if  guess==answer:
    print("you have ",count ," left ")
    break 
  elif guess<answer:
    print("it is greater  that ",guess)
  elif guess>answer:
    print("it is less  that ",guess)

print("the answer is ",answer)