# Random Library 
import random

attempts = 5
number = random.randint(1, 10)
print("**********GUESS THE NUMBER************")
while attempts > 0:
    try:
        guess = int(input("Enter a number between 1 and 10: "))
        
        if guess < number:
            print("Your guess is less than the number.")
        elif guess > number:
            print("Your guess is greater than the number.")
        else:
            print("Correct! You guessed the number!")
            break
        

        attempts -= 1
        print("Attempts left:", attempts)

    except:
        print("Invalid input! Please enter a number.")

        attempts -= 1
        print("Attempts left:", attempts)

if attempts == 0:
    print("Attempts over! The number was", number)





