def calculate(a,b,o):
    if(o == '+'):
        return a+b
    elif o == '-':
        return a-b
    elif o == '*':
        return a*b
    elif o =='/':
        if(b==0):
            print("division by 0 not possible!")
            return
        return a/b
while True:
    c= "yes"
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter a operator + - * or / : ")
    print(calculate(num1,num2,operator))
    c = input("Continue? ")
    if(c.lower() != "yes"):
        break