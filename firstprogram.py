import random
coinFaces = ['Head','Tail']


randomChoice = random.choice(coinFaces)

print(randomChoice)

userChoice = input('Choose Head or Tail : ')

if(userChoice.lower() == randomChoice.lower()):
    print('you won the toss')
else:
    print('you lost, try again')