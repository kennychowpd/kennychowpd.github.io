from operator import countOf

def main():
    user_input = input("Give me an arithmetic expression: ").strip().lower()
    
    answer = round(calcu(user_input), 1)
    
    print(answer)
    
def calcu(text):
    operator = ["+", "-", "*", "/"]
    counter = 0
    if any(i in text for i in operator):
        for i in text:
            if i in operator:
                counter += 1
    if counter == 1:
        op_used = list(set(text) & set(operator))[0]
        text = text.split(op_used)
        num2 = int(text[1])
        num1 = int(text[0])
        if op_used == "+":
            return float(num1 + num2)
        if op_used == "-":
            return float(num1 - num2)
        if op_used == "*":
            return float(num1 * num2)
        if op_used == "/":
            return float(num1 / num2)
             
    else:
        print("Please use only 1 operator, which can be +, -, * or /")
        main()
        
main()
        
    