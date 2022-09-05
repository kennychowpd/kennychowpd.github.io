import random


class Hat:
    companies = ["Apple", "Tesla", "Google", "Amazon"]

    @classmethod
    def sort(cls, name):
        companies = random.choice(cls.companies)
        print(name, "is in", companies)


Hat.sort("Kenny")
