# EA 3
# Last Updated summer 2024
# Luis Nigoa 

# CHAPTER 6 

# 1. Write a function called enrolled that just prints the following: I was enrolled in CIS156 during Fall 2023.
# No arguments should be passed into the function and the function should not return a value (2 pts.).
def enrolled():
    print("I was enrolled in CIS156 during Fall 2023.")
    
# 2. Write a statement to call the enrolled function (1 pt.).
enrolled()

# 3. Write a function named greeting. The function should accept ONE argument, the
# name of the person you are greeting and PRINT the following: Hello <name argument>, it is great to meet you!
# The function should not return a value (2 pts.).
def greeting(name):
    print(f"Hello {name}, it is great to meet you!")
# 4. Write a statement to call the greeting function passing in an argument of Charmander (1 pt.).
greeting("Juan")
# 5. Write a statement to call the four_args function passing in a value of 12 that will be assigned to parameter a,
# a value of 6.2 that will be assigned to parameter b, a value of -20 that will be assigned to parameter c
# and a value of 21 that will be assigned to parameter d. 
# Save the returned answer in a variable named returned_value. Print returned_value (4 pts.).
def four_args(a, b, c, d):   # DO NOT DELETE OR UPDATE THIS FUNCTION
    answer = a + b * c + d   # DO NOT DELETE OR UPDATE THIS FUNCTION
    return answer   # DO NOT DELETE OR UPDATE THIS FUNCTION
return_vallue= four_args(12, 6.2, -20, 21)
print(return_vallue)


