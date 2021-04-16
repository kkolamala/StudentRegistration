import random

randomNumber = random.randint(1,100)

print(randomNumber)

isGuess = False

counter = 0
maxAttempts = 5

while not isGuess:
    counter += 1
    userGuess = int(input('enter your guess betweeen 1 - 100: '))
    if userGuess == randomNumber:
        print('you guessed correctly')
        isGuess = True
    elif counter == maxAttempts and not isGuess:
        print('Try again, you ran out of your %d attempts'% maxAttempts)
    elif userGuess < randomNumber:
        print('your guess is low')
    else:
        print('your guess is high')

    
        
       
    
    
        
    
    

    




