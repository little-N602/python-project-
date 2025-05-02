# EA 5
# Enter your name

# Last updated 10/04/2023

# CHAPTER 8

# 1. Assign any whole number to variable var_1 (1 pt.).
var_1 = 19

# 2. Write an if statement that assigns 15 to the variable var_2 and -10 to the variable var_3
# and prints the sum of var_2 and var_3, if the variable var_1 is less than or equal to 15 (3 pts.).
if var_1 <= 15:
    var_2 = 15
    var_3 = -10
    print(var_2 + var_3)
# 3. Assign any whole number to var_4 (1 pt.).
var_4 = 15

# 4. Write an if-else statement that prints out 'Yes, you definitely can', if var_4 is greater than 20 and
# prints out 'Nope.' if it is not greater than 20 (3 pts.).
if var_4 > 20:
    print('Yes, you definitely can')
else:
    print('Nope.')
# 5. Assign any positive whole number to pulseRate (1 pt.).
pulseRate = 69

# 6. Write an if-else statement that prints 'Your pulse is normal' if pulseRate
# is within the range of 60 to 100, inclusively. If pulse is outside the range, print 'Your pulse rate may warrant further investigation by a medical professional' (4 pts.).
if 60<= pulseRate<=100:
    print( 'Your pulse is normal')
else:
    print('Your pulse rate may warrant further investigation by a medical professional')
# 7. Use the try except keywords to verify that a user has entered a valid int value by
# prompting the user to enter an integer.  If the value is a valid integer, print out 'You entered a valid integer'.
# If the value is not a valid integer print out 'That is not a valid integer' (3 pts.).
try:
    input1 = input("please enter a integer")
    value= int(input1)
    print("You entered a valid integer")
except ValueError:
    print('That is not a valid integer')
# 8. Import the random module and generate two random integer numbers. The first random number
# should be between -32 and -75 and the second random number should be between 32 and 92.
# Print both random numbers (4 pts.).
import random
random_numbern = random.randint(-75,-32)
random_numberp = random.randint(32,92)
print(f"random_numbern (between -32 and -75): {random_numbern} " )
print(f"random_numberp (between 32 and 92): {random_numberp}" )
# 9. Import the random module and generate five random integer numbers. 
# Each random number should be between 1 and 25
# Print all five random numbers PLUS the average value of the random numbers (5 pts.).
import random
random_numbers = [random.randint(1,25)for _ in range(5)]
print("random_numbers:", random_numbers)
average_v = sum(random_numbers) / len(random_numbers)
print("Average value:", average_v)