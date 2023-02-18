"""
Student class

This class stores methods for different types of students
"""
class Student:
    """
    Constructor method for the Student class

    Parameters:
    name (string): name of the student
    age (int): age of the student
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    """
    Display method for the Student class

    Prints a formatted string with the students name and age
    """
    def display(self):
        print(f"The student {self.name} is {self.age} years old")
"""
Engineer class

This class inherits from the student class and stores methods for an engineer student
"""
class Engineer(Student):
    """
    Constructor method for the Engineer class

    Parameters:
    name (string): name of the student
    age (int): age of the student
    courses (string): course the student is taking 
    """
    def __init__(self, name, age, courses):
        super().__init__(name, age)
        self.courses = courses
    """
    Display method for the Engineer class

    Prints a formatted string with the engineers name, age, and the course being taken
    """
    def displayEngineer(self):
        print(f"The engineer named {self.name} is {self.age} years old and has taken {self.courses} in school.")
"""
Doctor class

This class inherits from the student class and stores methods for a doctor
"""
class Doctor(Student):
    """
    Constructor method for the Doctor class

    Parameters:
    name (string): name of the doctor
    age (int): age of the doctor
    hospital (string): hospital the doctor works at
    """
    def __init__(self, name, age, hospital):
        super().__init__(name, age)
        self.hospital = hospital
    """
    Display method for the Doctor class

    Prints a formatted string with the doctors name, age, and hospital
    """
    def displayDoctor(self):
        print(f"The doctor named {self.name} is {self.age} years old and works at {self.hospital}.")

"""
Main function

This creates an instance of the object E in the Engineer class and passes through parameters with E.displayEngineer(). Creates an instance of teh object D in the Doctor class and passes through parameters with D.displayDoctor()
"""
def main():

    E = Engineer("Matt", 24, "Foundations of Programming")
    E.displayEngineer()

    D = Doctor("Jane", 36, "Lowell General Hospital")
    D.displayDoctor()

if __name__ == "__main__":
    main()