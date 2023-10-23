# Hierarchical inheritance is phenomenon where two or more derived class inherite from common base class that share common properties and methods .
# Base class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}"

# Derived class 1
class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display_info(self):
        return f"Manager - {super().display_info()}, Team Size: {self.team_size}"

# Derived class 2
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_languages):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages

    def display_info(self):
        return f"Developer - {super().display_info()}, Languages: {', '.join(self.programming_languages)}"

# Derived class 3
class Designer(Employee):
    def __init__(self, name, employee_id, salary, design_tools):
        super().__init__(name, employee_id, salary)
        self.design_tools = design_tools

    def display_info(self):
        return f"Designer - {super().display_info()}, Tools: {', '.join(self.design_tools)}"

# Demonstrate hierarchical inheritance
if __name__ == "__main__":
    manager = Manager("Alice", "M123", 80000, 5)
    print(manager.display_info())

    developer = Developer("Bob", "D456", 70000, ["Python", "JavaScript", "Java"])
    print(developer.display_info())

    designer = Designer("Eva", "D789", 75000, ["Adobe Photoshop", "Sketch", "Figma"])
    print(designer.display_info())
