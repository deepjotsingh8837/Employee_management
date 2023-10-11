from validations import *


class Employee:
  empDict = {}

  def __init__(self, emp_id, name, dob, age, gender, phone, address, city,
               salary, pan_card, aadhar, department, designation):
    self.emp_id = emp_id
    self.name = name
    self.dob = dob
    self.age = age
    self.gender = gender
    self.phone = phone
    self.address = address
    self.city = city
    self.salary = salary
    self.pan_card = pan_card
    self.aadhar = aadhar
    self.department = department
    self.designation = designation
    if self.department in self.empDict.keys():
      self.empDict[self.department].append(self.name)
    else:
      self.empDict[self.department] = [self.name]

  def display(self):
    print(self.emp_id, " ", self.name, " ", self.age, " ", self.gender, " ",
          self.address, " ", self.city, " ", self.salary, " ", self.pan_card,
          " ", self.aadhar, " ", self.department, " ", self.designation)

  def get_salary(emp):
    return emp.salary

  @classmethod
  def departmentWiseDetails(self):
    for k, v in self.empDict.items():
      print(k, " = ", v)


empList = []
obj = Employee('101', 'Deepjot', '11/04/2001', '22', 'Male', '9592068383',
               'F501', 'Pune', '22000', 'ABCDE1234A', '123456789090', 'it',
               'manager')
empList.append(obj)

while True:
  print("")
  print("1. Press 1 for adding records")
  print("2. Press 2 for displaying records")
  print("3: Press 3 for searching the employee")
  print("4. Press 4 for the Department wise name of the Employees")
  print("5. Press 5 for deleting the record of the Employee")
  print("6. Press 6 for updating the record of the Employee")
  print("7. Press 7 To display the details of employee with highest salary")
  print("8. Press 8 To display the details of employee with lowest salary")
  print("9. Press 9 for exit")
  ch = int(input("enter your choice: "))
  if ch == 1:
    while True:
      emp_id = input("enter the employee id: ")
      if validate_employee_id(emp_id):
        break
      else:
        print("Please!!! enter the correct Employee Id")

    while True:
      name = input("Enter the employee  name : ")
      if validate_name(name):
        break
      else:
        print("Please!!! enter the name correctly")
    while True:
      dob = input("Enter the Date of Birth of the employee: ")
      if validate_dob(dob):
        break
      else:
        print("Enter the correct date of birth.")
    while True:
      age = input("Enter the age: ")
      if validate_age(age):
        break
      else:
        print("Please!!! enter the correct age")
    while True:
      gender = input("Enter the gender: ")
      if validate_gender(gender):
        break
      else:
        print("Please!!! enter the coorect gender")
    while True:
      phone = input("Enter the employees Phone Number: ")
      if validate_phone_number(phone):
        break
      else:
        print("Enter the correct phone number.")

    address = input("Enter the employee address: ")

    while True:
      city = input("Enter the city: ")
      if validate_city(city):
        break
      else:
        print("Please!!! enter the correct city")
    while True:
      salary = input("Enter the salary: ")
      if validate_salary(salary):
        break
      else:
        print("Please!!! enter the salary correctly")
    while True:
      pan_card = input("Enter the employee Pan Card Number: ")
      if validate_PAN(pan_card):
        break
      else:
        print("Please!!! enter the pan number correctly")

    while True:
      aadhar = input("Enter the aadhar card number: ")
      if validate_aadhar(aadhar):
        break
      else:
        print("Please!!! enter the aadhar number correctly")
    while True:
      department = input("Enter the department name: ")
      if validate_department(department):
        break
      else:
        print("Please!!! enter the department name correctly")
    while True:
      designation = input("Enter the employee's designation: ")
      if validate_designation(designation):
        break
      else:
        print("Please!!! enter the designation correctly")
    obj = Employee(emp_id, name, dob, age, gender, phone, address, city,
                   salary, pan_card, aadhar, department, designation)
    empList.append(obj)

  elif ch == 2:
    for i in empList:
      i.display()

  elif ch == 3:
    while True:
      print("Press A : To search the Employee by the Employee ID")
      print("Press B : To search the employee by their Name")
      print("press C : To search the employee by their Department")
      print("Press D : To exit the Searching Window")
      ch1 = input("Enter the choice: ")
      if ch1 == 'A':
        p = input("Enter the Employee ID to be searched: ")
        for i in empList:
          if i.emp_id == p:
            i.display()
          else:
            print("!!!Please enter the correct Employee ID!!!")
      elif ch1 == 'B':
        p = input("Enter the name of the Employee to be searched: ")
        for i in empList:
          if i.name == p:
            i.display()
          else:
            print("!!!Please enter the correct Name!!!")
      elif ch1 == 'C':
        p = input(
            "Enter the name of the department in which Employee is working: ")
        for i in empList:
          if i.department == p:
            i.display()
          else:
            print("!!!Please enter the correct Department!!!")
      elif ch1 == 'D':
        break
  elif ch == 4:
    Employee.departmentWiseDetails()
  elif ch == 5:
    while True:
      print("Press A : To delete the record by Employee Id")
      print("Press B : To delete the record by Name of the Employee")
      print("Press C : To exit the deletion window")
      ch2 = input("Enter your Choice")
      if ch2 == 'A':
        p = input("Enter the Employee ID")
        for i in empList:
          if i.emp_id == p:
            empList.remove(i)
            print("Employee deleted successfully")
          else:
            print("!!!Enter the correct Employee ID!!!")

      elif ch2 == 'B':
        p = print("Enter the name of the employee")
        for i in empList:
          if i.name == p:
            empList.remove(i)
            print("Employee deleted sucessfully")
          else:
            print("!!!Enter the correct Name of the Employee!!!")
      elif ch2 == 'C':
        break

  elif ch == 6:
    while True:
      print("Update Employee Details: ")
      print("1. Update name of Employee")
      print("2. Update address of Employee")
      print("3. Update DOB of Employee")
      print("4. Update salary of Employee")
      print("a. Update salary of specefic employee by Employee Id")
      print("b. Update salary of all Employees working in specefic Department")
      print("c. Update the salary of all Employees")
      print("5: To exit the update window: ")
      ch3 = input("Enter your choice : ")
      if ch3 == '1':
        emp_id = input("Enter Employee ID to update name: ")
        new_name = input("Enter new name: ")

        for i in empList:
          if i.emp_id == emp_id:
            
            i.name = new_name
            print("Name updated successfully")

      elif ch3 == '2':
        emp_id = input("Enter the Employee ID to update address: ")
        new_address = input("Enter the address: ")
        for i in empList:
          if i.emp_id == emp_id:
            i.address = new_address
            print("Address updated successfully")
      elif ch3 == '3':
        emp_id = input("Enter Employee ID to update DOB: ")
        new_dob = input("Enter the DOB: ")
        for i in empList:
          if i.emp_id == emp_id:
            i.dob = new_dob
      elif ch3 == '4':
        emp_id = input("Enter Employee ID to update salary: ")
        new_salary = input("Enter the salary: ")
        for i in empList:
          if i.emp_id == emp_id:
            i.salary = new_salary
            print("Salary updated successfully")
      elif ch3 == 'a':
        emp_id = input(
            "Enter Employee ID to update salary of specefic Employee: ")
        new_salary = float(input("Enter the salary: "))
        for i in empList:
          if i.emp_id == emp_id:
            i.salary = new_salary
            print("Salary updated successfully")

      elif ch3 == 'b':
        department = input("Enter name of department to update salary: ")
        new_salary = int(input("Enter the salary: "))
        for i in empList:
          if i.department == department:
            i.salary = new_salary
            print("salary updated successfully")
      elif ch3 == 'c':
        new_salary = int(input("Enter the amount to be updated: "))
        for i in empList:
          i.salary = new_salary
          print("Salary Updated Successfully")
      elif ch3 == '5':
        break

  elif ch == 7:
    highest_salary_employee = max(empList, key=Employee.get_salary)
    print("Details of the employee with the Highest salary: ")
    highest_salary_employee.display()
  elif ch == 8:
    lowest_salary_employee = min(empList, key=Employee.get_salary)
    print("Details of the employee with the Lowest salary: ")
    lowest_salary_employee.display()

  elif ch == 9:
    print("Exiting the Employee Management System. Goodbye!")
    break
  else:
    print("Invalid choice")
    
