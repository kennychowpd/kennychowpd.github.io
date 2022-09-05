class Person:
    def __init__(self, name, company=None, skill=None):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.company = company
        self.skill = skill

    def __str__(self):
        return f"{self.name} from {self.company}"
    
    def work(self):
        match self.skill:
            case "Python":
                return "🐍"
            case "Javascript":
                return "🟨"

    @classmethod
    def get(cls):
        name = input("Name: ")
        company = input("Company: ")
        skill = input("Skill: ")
        return cls(name, company, skill)
    
    # @property # Getter
    # def company(self): 
    #     return self._company # convention so it doesn't mix up with the og
    
    # @company.setter # Setter
    # def company(self, company): # check in case the value is changed in the code
    #     if company not in ["Apple", "Tesla", "Amazon", "Google"]:
    #         raise ValueError("Not the person we are looking for")
    #     self._company = company  # convention so it doesn't mix up with the og
        
    
                

def main():
    person = Person.get()
    print(person)
    # person.company = "Meta" # the Getter & Setter will get call and raise an error
    print(person.work())
    

if __name__ == "__main__":
    main()
