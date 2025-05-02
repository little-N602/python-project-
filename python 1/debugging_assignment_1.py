# Your name
# DA_1

# This program reads an unspecified number of integers, determines how many positive 
# and negative values have been read, and computes the total and average of the input values 
#  (not counting zeros). The program ends when a zero is inputted.
# The average should be formatted as a fixed-point number with 2 decimal places.

# Prompt user to enter an integer
number = int(input("Enter an integer, the input ends if a zero is entered: ")) # for got to add the closing () for the program
count_positive = 0
count_negative = 0
count = 0
total = 0 # forgot to add a O so when the program start it would state with nothing in totol 

# While loop to read and count numbers
while number !=0:
    if number > 0:
        count_positive += 1
    elif number < 0:
        count_negative += 1 # has the increment to count set to 1 instead of 2 every time you put a negative 2 

    total += number
    count += 1
# Prompt user to enter another integer    
    number = int(input("Enter an integer, the input ends if a zero is entered: "))
#need to make sure that the code was properly integreated in the loop comand 
# Display output
if count == 0:
    print("No numbers were entered except zero")
else:
    print(f"The number of positives is {count_positive}")
    print(f"The number of negatives is {count_negative}") # need to add a s on negative so it print the corret statemnt 
    print(f"The total is {total}" )
    print(f"The average is {total / count:.2f}") # add command that has 2 decimal places for the outcome     
