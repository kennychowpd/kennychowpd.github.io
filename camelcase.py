import re
user_input = input("Enter a camel case variable name: ")
splited_input = re.split("(?=[A-Z])", user_input)
reassumbled_input = "_".join(splited_input).lower()
print(reassumbled_input)