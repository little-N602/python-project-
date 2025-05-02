# EA 4
# Luis Nigoa 
# Last updated summer 2024

# CHAPTER 6 (loops and loops within functions)

# 1. Write a while loop that adds the variable number to to the variable sum_of numbers.  Then it should prompt the user with text
# to enter another whole number (int) and add it to sum_of_numbers. The loop should iterate as long as the user
# enters an even whole number. The whole number can be positive or negative.
# Print sum_of_numbers AFTER EXITING the while loop (4 pts.).
sum_of_numbers = 0 # DO NOT DELETE THIS LINE OF CODE, USE THE VARIABLE IN THE WHILE LOOP
number = int(input('Enter a whole number: ')) # DO NOT DELETE OR MODIFY THIS LINE OF CODE
# The while loop should appear after this comment
while number % 2 == 0:
 sum_of_numbers += number
 number = int(input('Enter a whole number: '))
print("sum_of_numbers", sum_of_numbers)
# 2. Write a for in loop to iterate over class_string, printing each letter on a separate line (2 pts.).
class_string = "PythonProgramming"  # DO NOT DELETE OR MODIFY THIS LINE OF CODE
for class_string in "PythonProgramming":
 print(class_string)

# 3. Write a for in loop that prints the numbers -4 through 10 on the same line with a comma after each number (3 pts.).
for n in range(-4, 11):
 if n == 10:
  print(n, end='')
 else:
  print(n, end=',')
    
# 4. Write a for in loop that prints the following set of numbers: 12 24 36 48 60 on one line with a space after each number
# by specifying the step value in the range. Step value is covered in the Exercise 6.4 video (3 pts.).
print() # DO NOT DELETE THIS LINE OF CODE
n = 12
while n < 61:
 print (n, end=' ')
 n += 12    
# 5. Write a nested for in loop similar to the loop found at the end of section 6.4. The outer loop's range should
# be between the numbers 1 through 5 inclusively using x as the variable. The inner loop's range should be
# between the numbers -5 through -1 inclusively using y as the variable.
# Print the values of x and y inside the inner loop on the same line (3 pts.). 
print() # DO NOT DELETE THIS LINE OF CODE
for x in range(1, 6):
 for y in range(-1, -6, -1):
  print(f"x = {x} and y = {y}")
# 6. Write a function that accepts two whole numbers as arguments
# First: to indicate a starting value
# Second: To indicate how many times the number will increase expoentially 
# The function will use the arguments to exponentially increase the starting number
# before the loop stops.
# The returned value should be printed to the console
# DO NOT USE a math built-in functions for this exercise
# (5 points)
def increase_expoentailly(start_value, exponets):
    result = 1
    for _ in range(exponets):
     result *= start_value
    return result
result = increase_expoentailly(9,7)
print(result)