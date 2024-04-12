class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.set_emp_id(emp_id)
        self.set_name(name)
        self.set_position(position)
        self.set_salary(salary)

    def get_emp_id(self):
        return self._emp_id

    def set_emp_id(self, emp_id):
        if isinstance(emp_id, int):
            self._emp_id = emp_id
        else:
            raise ValueError("Employee ID must be an integer.")

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name must be a string.")

    def get_position(self):
        return self._position

    def set_position(self, position):
        if isinstance(position, str):
            self._position = position
        else:
            raise ValueError("Position must be a string.")

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be a non-negative number.")





def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

if __name__ == "__main__":
    main()
