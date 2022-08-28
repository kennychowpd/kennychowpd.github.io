from pyfiglet import Figlet, FontNotFound
import sys

f = Figlet()
argv_len = str(len(sys.argv))

match argv_len:
    case "1":
        user_input = input("Input: ")
        print(f.renderText(user_input))
    case "3":
        try:
            f = Figlet(font = sys.argv[2])
            user_input = input("Input: ")
            print(f.renderText(user_input))
        except FontNotFound:
            print("Invalid usage")
            sys.exit()
    case other:
        print("Invalid usage")
        sys.exit()
