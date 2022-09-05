class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        
#inheritance: a class getting everything from its superclass
class Student(Wizard): # Wizard is Student's superclass
    def __init__(self, name, house):
        super().__init__(name) # initiate the superclass
        self.house = house
        
        
class Professor(Wizard): 
    def __init__(self, house):
        super().__init__(name)
        self.subject = subject
        
Wizard = Wizard("Kenny the donothing") # using Wizard class to construct an obj 
student = Student("Harry", "7-11")  # using Student class with Wizard superclass to construct an obj
professor = Professor("Severus", "Sorting shelves quickly")