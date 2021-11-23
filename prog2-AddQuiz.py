# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

user = input("Hi! Please enter your name to proceed: ")
print(f"Hi {user}! You are going to answer 10 random Question. Lets get started! ")

import random
# generate two random numbers to add from (0 to 99)
def randomAdd():
    Num1 = random.randint(0,99)
    Num2 = random.randint(0,99)
    RanAnws = Num1 + Num2
    print(f"What will be the sum if {Num1} is added to {Num2}?")
    return RanAnws

# evaluate the user answer if correct
def userAns():
    global randAns
    randAns = randomAdd
    userAns = int(input("Enter your answer: "))
    return randAns == userAns


    