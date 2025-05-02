#Luis nigoa
# PA 9


class Employee:
    # define each area of information that theuser would need to input and how they would need to input 
    def __init__(self, empl_number: int, name: str, department: str, yearly_salary: int):
        """
        Initializes an Employee with the provided empl_number, name, department, yearly_salary.
        :param empl_number: int, the employee work number
        :param name: str, the name of the employee
        :param department: str, the department where the employee would work
        :param yearly_salery: int, the yearly salary the employee makes
        """
        self.empl_number = empl_number
        self.name = name
        self.department = department
        self.yearly_salary = yearly_salary
# return the infromation that is define to the couter part that is lable for the user to input the information
# Then return the information they input 
    def __str__(self): 
        """
        Returns a string representation of the employee object.
        :return: str, the string describing the employee info 
        """
        return (f"Employee Information:\n"
                f"Employee Number: {self.empl_number}\n"
                f"Employee Name: {self.name}\n"
                f"Employee's Department: {self.department}\n"
                f"Yearly Salary: ${self.yearly_salary:,}")  
# allow you to update the salery that you are trying to input in the department  
    def update_salery(self, new_salery: int):
        """
        Updates the yearly salary of the employee.
        :param new_salery: int, the new yearly salary for the employee
        """
        self.yearly_salary = new_salery
# allow you to update the depatment name of employee if need be 
    def update_department(self, new_department: str):
        """
        Updates the department of the employee.
        :param new_department: str, the new department for the employee
        """
        self.department = new_department
#this part of the code the user would need to enter in the information that they would need to enter of the employee
# they cant enter information blank where it will tell them they need to enter they information
if __name__ == '__main__':
    print("Enter the employee information: ")
    while True:
        try:
            empl_number = int(input("Enter the employee number: ")) 
            break
        except ValueError:
            print("Invalid input. Employee number must be an integer.")

    while True:
        name = input("Enter the employee name: ")
        if name.strip():
            break
        else:
            print("Name cannot be blank. Please enter a valid name.")

    while True:       
        department = input("Enter the employee's department: ")
        if department.strip():
            break
        else:
            print("Department cannot be blank. Please enter a valid department name.")

    while True:
        try:        
            yearly_salary = int(input("Enter the employee's yearly salary: ").replace(',', ''))  
            break
        except ValueError:
            print("Invalid input. Yearly salary must be a valid number.")
# define what the user input in each category and print out the information they printed inputed
    employee = Employee(empl_number, name, department, yearly_salary)
    print("\n" + str(employee))
#update the amount of on the salery of the finance department.
    employee.update_department("Finance")
    employee.update_salery(75000)
#will print out how the information has be updated with the record shown below  
    print("\nUpdated Employee Information:")
    print(employee)
