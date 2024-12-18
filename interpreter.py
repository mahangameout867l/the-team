num1,op,num2=input("Expression:").split(" ")
#print(num1)
#print(num2)
#print(op)
num1=float(num1)
num2=float(num2)
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/" or "%":
    print(num1 / num2) or (num1 % num2)