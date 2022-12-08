def calc():
    n1 = int(input("Please enter first Num: "))
    n2 = int(input("Please enter sec Num: "))
    op = input("please enter op: ")

    if op == "*":
        print(n1*n2)
    elif op == "+":
        print(n1+n2)
    elif op == "/" and n2 == 0:
        print("Zero Division Error")
    elif op == "/":
        print(n1/n2)
    elif op == "-":
        print(n1-n2)
    else:
        print("Not defined Operator")


calc()