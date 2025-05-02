#Luis Nigoa
# DA_1


#the the first prompt make it where if the person trys to input a non number to the code it will tell them to enter a a number 
# it has the try and except method where if they try to input someing like a @ symbol or a letter it will send them a error message 

def get_integer(prompt):
    while True:
        try:
            
            return int(input(prompt))
        except ValueError:
            print("enter a vailid input numnber")
#the second prompt is for the name were the basic run through would only allow a name to be enter
# the if raise statement are use just incase for certain thing like the first one for if they try to put nothing for a name then they get an error message
# if they put an @ symbol or other they would get another error message             
def get_input(prompt):
    while True:
        try:
            value = input(prompt)
            if not value.strip():
                 raise ValueError("can't leave it blank")
            if not value.isalpha():
                raise ValueError("must be a letter name")
            return value
        except ValueError as e:
            print("enter an actural name")
x = get_integer("Please enter a number: ")

y = get_input("Please enter your name: ")# was defind for x an use the varieble int even though this part of code dosn't use numnbers 

print(x)
print(y) #was undefind