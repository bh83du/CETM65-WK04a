'''
Create a Employee Class
'''
class Employee():

# Define the details for the Employee class
    def __init__(self, name,dob,emp_id):
        self.name = name
        self.dob = dob
        self.id = emp_id


# Add a __str__ method to give a Human readable desciption of the class. 
    def __str__(self):
        return "This is the Employee Class __str__"

# Add a __repr__ method to return the Class used to create the object
    def __repr__(self):    
        return "Employee(self, name,dob,emp_id)"

# Method to display the Employee's information

    def display(self):
        print('\n') # Inserts new line.
        print("The Employee's name is: " + self.name)
        print("The Employee's date of Birth is " + self.dob)
        print("The Employee's ID is " + self.id)
        print("\n")

'''
Create a Sub Class of Employee for Temporary Employees
'''

class Temporary(Employee):

    number_of_temp_emp = 0  # Class variable to allow tracking of number of Employees

    def __init__(self, name, dob, emp_id):
        super().__init__(name, dob, emp_id) # Attributes inherited from Employee Class
        self.hourlyrate = None              # Hourly Rate specific to Temporary Class
        self.weeklyhours = None             # Weekly Hours specific to Temporary Class
        self.tgp = None                     # Temporary Gross Weekly Pay
        Temporary.number_of_temp_emp = Temporary.number_of_temp_emp + 1  # Add to running total of Temporary Employees

# Add a __str__ method to give a Human readable desciption of the class. 

    def __str__(self):
        return "This is the Temporary Employee Class __str__method"

# Add a __repr__ method to return the Class used to create the object

    def __repr__(self):
        return "Temporary(self, name,dob,emp_id)"

# Method to calculate the gross weekly wage of the Employee

    def salary_info(self):
        self.tgp = (self.hourlyrate * self.weeklyhours)
        print('\n')
        print(f'Contract Type is Temporary')
        print(f'Employee hourly rate is: £{self.hourlyrate}')
        print(f'Employee contracted weekly hours are: {self.weeklyhours} hours')
        print(f'Employee gross weekly salary is: £{self.tgp}')



'''
Create a Sub Class of Employee for Permanent Employees
'''

class Permanent(Employee):

    number_of_perm_emp = 0 # Class variable to allow tracking of number of Employees


    def __init__(self, name, dob, emp_id, ):
        super().__init__(name, dob, emp_id) # Attributes inherited from Employee Class
        self.annualsalary = None            # Annual Salary specific to Permanent Class
        self.pensionplan = None             # Pension Plan Status for Permanent Class
        self.pgp = None                     # Permanent Gross Weekly Pay
        # Increment the number of permanent employees by 1
        Permanent.number_of_perm_emp = Permanent.number_of_perm_emp + 1

# Add a __str__ method to give a Human readable desciption of the class. 

    def __str__(self):
        return "This is the Permanent Employee Class __str__ method"

# Add a __repr__ method to return the Class used to create the object

    def __repr__(self):
        return "Permanent(self, name,dob,emp_id)"

# Add a method to calculate the Permanent Gross Weekly salary
    def salary_info(self):
        self.pgp = (self.annualsalary / 52)
        print('\n')
        print(f'Contract Type is Permanent')
        print(f'Employee Annual Salary is: £{self.annualsalary}')
        print(f'Employee Pension Scheme Status: {self.pensionplan}')
        print(f'Employee gross weekly salary is: £{self.pgp}')


# Create an Employee   

john=Temporary('John Wall', '19/06/1975', 'E0001')
john.hourlyrate = float(5.55)
john.weeklyhours = float(37.5)

stuart=Permanent('Stuart Riding', '06/06/1975', 'E0002')
stuart.annualsalary = 36000
stuart.pensionplan = "Member"

#Program to access the data

active = True

while active == True:
    print("\n")
    print("Please choose from the following options: ")
    print("\n")
    print("1. Class Details")
    print("2. Employee Numbers")
    print("3. Employee Details")
    print("\n")
    command = input("> ")
    #Check the command entered
    if command == "1": # Print the Class Details.  Display the output of the __str__ methods for each sub-class
        print(stuart)
        print(john)
    elif command == "2": # Print the Employee Numbers
        all = int(Temporary.number_of_temp_emp) + int(Permanent.number_of_perm_emp)
        print(f"Total number of Temporary Employees: {Temporary.number_of_temp_emp}")
        print(f"Total number of Permanent Employees: {Permanent.number_of_perm_emp}")
        print(f"Total number of Employees: {all}")        
    elif command == "3": #Enter a second loop to access Employee Details
        print("\n")
        print("Select your Employee:") # Select which Employee details you wish to see
        print("1. John Wall")
        print("2. Stuart Riding")
        selection = input("> ")
        if selection == "1":
            john.display() # Display the Employee's Personal Data.  Method from the Parent Class
            john.salary_info() # Display the Employee's Salary datat.  Method fromt he Sub Classe 
        elif selection == "2":
            stuart.display()  # Display the Employee's Personal Data.  Method from the Parent Class
            stuart.salary_info() # Display the Employee's Salary datat.  Method fromt he Sub Classe 
        else:
            print("Invalid ID.  Please try again.") # Invalid Employee entered.  Start Again
    else:
        active = False  # Press any other button, and the programme ends