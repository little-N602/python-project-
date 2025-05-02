# EA 7
#  Luis nigoa

# Last updated 10/04/2023

# CHAPTER 9 and Sets


# 1. Create a dictionary called birthdays, that includes the person's name as the key and their birthday as the value.
# The names and birthdays should be stored as strings (3 pts.).
# The dictionary should contain: Mike - 02/01/1990, Sandra - 03/15/1992, Yuki - 05/25/1987,
# Kimberley - 05/25/1987, Ira - 12/03/1985
birthdays = {
    "Mike": "02/01/1990",
    "Sandra": "03/15/1992",
    "Yuki": "05/25/1987",
    "Kimberley": "05/25/1987",
    "Ira": "12/03/1985"
}

# 2. Print the dictionary (1 pt.).
print(birthdays)

# 3. Write a for in loop that prints the keys in the dictionary (2 pts.).
for key in birthdays:
    print(key)
# 4. Write a for in loop that prints the values in the dictionary (2 pts.).
for key in birthdays:   
    print(birthdays[key])

    
# 5. Write a for in loop that assigns the keys and values to seperate variables and prints the following
# line for each user in the dictionary: "Person name has a birthday of birthday."
# eg. Person Kimberley has a birthday of 05/25/1987. (3 pts.)
for person, birthday_date in birthdays.items():
    print(f"Person {person} has a birthday of {birthday_date}")

# 6. Write an if statement using the keywords not in to determine if user name Daniel is in the dictionary.  If Daniel is not in the dictionary,
# print out "Person Daniel is not in the dictionary.", else print out "User Daniel is in the dictionary." (2 pts.).
if "Daniel" not in birthdays:
    print("Person Daniel is not in the dictionary.")
else:
    print("User Daniel is in the dictionary.")


# 7. The birthday was incorrect for Yuki.  Their birthday is actually 07/25/1987. Update Yuki's entry in the dictionary to reflect the birthday correction (1 pt.).
birthdays["Yuki"] = "07/25/1987"
print(birthdays)

# 8. Add person Joe with a birthday of 10/24/1945 to the dictionary and add Margaret with a birthday of 04/16/1980 to the dictionary (2 pts.).
birthdays["Joe"] = "10/24/1945"
birthdays["Margaret"] = "04/16/1980"
print(birthdays)
# 9. Person Sandra has retired, remove their entry from the dictionary.  Print the dictionary (2 pts.).
del birthdays["Sandra"]
print(birthdays)
##### Questions below do not relate to the scenario above #####


# 10. Write code to create a set named set_a with the following floats: 1.50, 36.32, 60.00, 72.68, 84.79 (2 pts.).
set_a = {1.50, 36.32, 60.00, 72.68, 84.79}

# 11. Write code to create a set named set_b with the following floats: 12.50, 24.75, 36.32, 48.84, 60.00 (2 pts.).
set_b = {12.50, 24.75, 36.32, 48.84, 60.00}

# 12. Write code that creates another set containing only the elements that are found in both set_A and set_b,
# and assigns the resulting set to the variable set_c.  Print set_c (2 pts.).
set_c = set_a & set_b
print(set_c)
# 13. Write code that creates another set containing all the elements of set_a and set_b, and assigns the
# resulting set to the variable set_d. Print set_d (2 pts.).
set_d = set_a | set_b
print(set_d)
# 14. Write code that creates another set containing the elements that appear in set_a but not in set_b,
# and assigns the resulting set to the variable set_e. Print set_e (2 pts.).
set_e = set_a - set_b
print(set_e)

# 15. Write code that creates another set containing the elements that are not shared by set_a and set_b,
# and assigns the resulting set to the variable set_f. Print set_f (2 pts.).
set_f = set_a ^ set_b
print(set_f)








