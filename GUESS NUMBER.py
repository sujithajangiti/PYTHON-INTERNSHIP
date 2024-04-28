import random
number=random.randint(1,100)

guess=0

while guess!=number:
    for i in range(10):
        guess=int(input("Enter Guess:"))

        if (guess < number):
            print("Guess higher")
        elif (guess > number):
            print("Guess lower")
        else:
            print("You Won!!")
            
    print("attempts over")