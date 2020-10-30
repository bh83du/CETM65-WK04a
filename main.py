'''
Module Docstring
'''


class Employee():
    '''
    Create a Employee Class
    '''
    # Define the details for the Employee class
    def __init__(self, name, dob, emp_id):
        self.name = name
        self.dob = dob
        self.emp_id = emp_id

# Add a __str__ method to give a Human readable desciption of the class.

    def __str__(self):
        return "This is the Employee Class __str__"

# Add a __repr__ method to return the Class used to create the object.

    def __repr__(self):
        return "Employee(self, name,dob,emp_id)"

# Method to display the Employee's information

    def display(self):
        '''
        Function Docstring
        '''
        print('\n')  # Inserts new line.
        print("The Employee's name is: " + self.name)
        print("The Employee's date of Birth is " + self.dob)
        print("The Employee's ID is " + self.emp_id)
        print("\n")


class Temporary(Employee):

    '''
    Create a Sub Class of Employee for Temporary Employees
    '''

    # Class variable to allow tracking of number of Employees
    no_of_temp_emp = 0

    def __init__(self, name, dob, emp_id):
        super().__init__(name, dob, emp_id)  # Inherited from Employee Class
        self.hourlyrate = None               # Specific to Temporary Class
        self.weeklyhours = None              # Specific to Temporary Class
        self.tgp = None                      # Temporary Gross Weekly Pay
        # Add to running total of Temporary Employees
        Temporary.no_of_temp_emp = Temporary.no_of_temp_emp + 1

    # Add a __str__ method to give a Human readable desciption of the class.

    def __str__(self):
        return "This is the Temporary Employee Class __str__method"

    # Add a __repr__ method to return the Class used to create the object

    def __repr__(self):
        return "Temporary(self, name,dob,emp_id)"

    # Method to calculate the gross weekly wage of the Employee

    def salary_info(self):
        '''
        Function Docstring
        '''
        self.tgp = (self.hourlyrate * self.weeklyhours)
        print('\n')
        print('Contract Type is Temporary')
        print(f'Employee hourly rate: £{self.hourlyrate}')
        print(f'Employee contracted weekly hours:{self.weeklyhours} hours')
        print(f'Employee gross weekly salary: £{self.tgp}')


class Permanent(Employee):
    '''
    Create a Sub Class of Employee for Permanent Employees
    '''
    # Class variable to allow tracking of number of Employees
    no_of_perm_emp = 0

    def __init__(self, name, dob, emp_id, ):
        super().__init__(name, dob, emp_id)  # Inherited from Employee Class
        self.annualsalary = None             # Specific to Permanent Class
        self.pensionplan = None              # Sepcific to Permanent Class
        self.pgp = None                      # Permanent Gross Weekly Pay
        # Increment the number of permanent employees by 1
        Permanent.no_of_perm_emp = Permanent.no_of_perm_emp + 1

# Add a __str__ method to give a Human readable desciption of the class.

    def __str__(self):
        return "This is the Permanent Employee Class __str__ method"

# Add a __repr__ method to return the Class used to create the object

    def __repr__(self):
        return "Permanent(self, name,dob,emp_id)"

# Add a method to calculate the Permanent Gross Weekly salary
    def salary_info(self):
        '''
        Function Docstring
        '''
        self.pgp = (self.annualsalary / 52)
        print('\n')
        print('Contract Type is Permanent')
        print(f'Employee Annual Salary: £{self.annualsalary}')
        print(f'Employee Pension Scheme Status: {self.pensionplan}')
        print(f'Employee gross weekly salary: £{self.pgp}')


# Create an Employee

john = Temporary('John Wall', '19/06/1975', 'E0001')
john.hourlyrate = float(5.55)
john.weeklyhours = float(37.5)

stuart = Permanent('Stuart Riding', '06/06/1975', 'E0002')
stuart.annualsalary = 36000
stuart.pensionplan = "Member"

# Program to access the data

ACTIVE = True

while ACTIVE is True:
    print("\n")
    print("Please choose from the following options: ")
    print("\n")
    print("1. Class Details")
    print("2. Employee Numbers")
    print("3. Employee Details")
    print("\n")
    command = input("> ")
    # Check the command entered
    if command == "1":
        # Print the Class Details.
        # Display the output of the __str__ methods for each sub-class
        print(stuart)
        print(john)
    elif command == "2":
        # Print the Employee Numbers
        all_emp = int(Temporary.no_of_temp_emp) + int(Permanent.no_of_perm_emp)
        print(f"Total No. of Temporary Employees:{Temporary.no_of_temp_emp}")
        print(f"Total No. of Permanent Employees:{Permanent.no_of_perm_emp}")
        print(f"Total No. of Employees: {all_emp}")
    elif command == "3":
        # Enter a second loop to access Employee Details
        print("\n")
        print("Select your Employee:")
        # Select which Employee details you wish to see
        print("1. John Wall")
        print("2. Stuart Riding")
        selection = input("> ")
        if selection == "1":
            john.display()
            # Display the Employee's Personal Data.  Method from Parent Class
            john.salary_info()
            # Display the Employee's Salary datat.  Method from Sub Class
        elif selection == "2":
            stuart.display()
            # Display the Employee's Personal Data.  Method from Parent Class
            stuart.salary_info()
            # Display the Employee's Salary datat.  Method from Sub Class
        else:
            print("Invalid ID.  Please try again.")
            # Invalid Employee entered.  Start Again
    else:
        ACTIVE = False
        # Press any other button, and the programme ends
