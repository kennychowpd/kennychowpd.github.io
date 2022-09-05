from datetime import date
import sys
import re
import inflect

inf_eng = inflect.engine()


class Birthday:
    def __init__(self, date):
        self.date = date

    def diff_in_min(self):
        birthday = date.fromisoformat(self.date)
        min_diff = (date.today() - birthday).days * 24 * 60
        return (
            inf_eng.number_to_words(min_diff).replace(" and", "").capitalize()
            + " minutes"
        )

    def __str__(self):
        return f"{self.date}"

    @classmethod
    def get(cls):
        date = input("Date of birth(YYYY-MM-DD): ")
        if not re.search(r"\d{4}-\d{2}-\d{2}", date):
            print("Invalid date")
            sys.exit()
        else:
            return cls(date)


def main():
    birthday = Birthday.get()
    print(birthday)
    print(birthday.diff_in_min())


if __name__ == "__main__":
    main()
