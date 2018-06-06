# an example for raw_input and int conversion
import random

number =  random.randint(1,10)

guess = 0

while guess != number:
    num1String = input('Guess the digit between 1 to 10 :')
    guess = int(num1String)
    if (guess > number):
        print ("Wrong! You guessed too high")
    if (guess < number):
        print ("Wrong! You guessed too low")
    if (guess == number):
        break

if guess == number:
    print("Guessed Right")





