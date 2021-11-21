# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# greetings
print ("Hello! This program can arrange four (4) numbers from highest to lowest.")

# ask inputs from the user
Num1 = float(input("Enter your first number: "))
Num2 = float(input("Enter your second number: "))
Num3 = float(input("Enter your third number: "))
Num4 = float(input("Enter your fourth number: "))

# possible outcome if the first number is the highest number
if Num1 >= Num2 >= Num3 >= Num4:
    print (f"Highest to Lowest: {Num1}, {Num2}, {Num3}, {Num4} ")
elif Num1 >= Num4 >= Num2 >= Num3:
    print (f"Highest to Lowest: {Num1}, {Num4}, {Num2}, {Num3} ")
elif Num1 >= Num3 >= Num4 >= Num2:
    print (f"Highest to Lowest: {Num1}, {Num3}, {Num4}, {Num2} ")
elif Num1 >= Num3 >= Num2 >= Num4:
    print (f"Highest to Lowest: {Num1}, {Num3}, {Num2}, {Num4} ")
elif Num1 >= Num2 >= Num4 >= Num3:
    print (f"Highest to Lowest: {Num1}, {Num2}, {Num4}, {Num3} ")
elif Num1 >= Num4 >= Num3 >= Num2:
    print (f"Highest to Lowest: {Num1}, {Num4}, {Num4}, {Num2} ")
    
# possible outcome if the second number is the highest number
elif Num2 >= Num3 >= Num4 >= Num1:
    print (f"Highest to Lowest: {Num2}, {Num3}, {Num4}, {Num1} ")
elif Num2 >= Num3 >= Num1 >= Num4:
    print (f"Highest to Lowest: {Num2}, {Num3}, {Num1}, {Num4} ")
elif Num2 >= Num4 >= Num3 >= Num1:
    print (f"Highest to Lowest: {Num2}, {Num4}, {Num3}, {Num1} ")
elif Num2 >= Num1 >= Num3 >= Num4 :
    print (f"Highest to Lowest: {Num2}, {Num1}, {Num3}, {Num4} ")
elif Num2 >= Num4 >= Num1 >= Num3:
    print (f"Highest to Lowest: {Num2}, {Num4}, {Num1}, {Num3} ")
elif Num2 >= Num4 >= Num3 >= Num1:
    print (f"Highest to Lowest: {Num2}, {Num4}, {Num3}, {Num1} ")
    
# possible outcome if the third number is the highest number
elif Num3 >= Num1 >= Num2 >= Num4:
    print (f"Highest to Lowest: {Num3}, {Num1}, {Num2}, {Num4} ")
elif Num3 >= Num2 >= Num1 >= Num4:
    print (f"Highest to Lowest: {Num3}, {Num2}, {Num1}, {Num4} ")
elif Num3 >= Num4 >= Num1 >= Num2:
    print (f"Highest to Lowestr: {Num3}, {Num4}, {Num1}, {Num2} ")
elif Num3 >= Num1 >= Num4 >= Num2:
    print (f"Highest to Lowest: {Num3}, {Num1}, {Num4}, {Num2} ")
elif Num3 >= Num2 >= Num4 >= Num1:
    print (f"Highest to Lowest: {Num3}, {Num2}, {Num4}, {Num1} ")
elif Num3 >= Num4 >= Num2 >= Num1:
    print (f"Highest to Lowest: {Num3}, {Num4}, {Num2}, {Num1} ")
    
#  possible outcome if the fourth number is the highest number
elif Num4 >= Num3 >= Num2 >= Num1:
    print (f"Highest to Lowest: {Num4}, {Num3}, {Num2}, {Num2} ")
elif Num4 >= Num2 >= Num3 >= Num1:
    print (f"Highest to Lowest: {Num4}, {Num2}, {Num3}, {Num1} ")
elif Num4 >= Num1 >= Num3 >= Num2:
    print (f"Highest to Lowest: {Num4}, {Num1}, {Num3}, {Num2} ")
elif Num4 >= Num3 >= Num1 >= Num2:
    print (f"Highest to Lowest: {Num4}, {Num3}, {Num1}, {Num2} ")
elif Num4 >= Num1 >= Num2 >= Num3:
    print (f"Highest to Lowestr: {Num4}, {Num1}, {Num2}, {Num3} ")
elif Num4 >= Num2 >= Num1 >= Num3:
    print (f"Highest to Lowest: {Num4}, {Num2}, {Num1}, {Num3} ")