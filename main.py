while True: 
    print("======= Calculator =======")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit\n")
    option = int(input("Enter choice: "))
    if option == 0:
        print("Program terminated.")
        break
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    if option == 1:
        print(f"Sum of {a} & {b} = {a+b}")
    elif option == 2:
        print(f"Difference of {a} & {b} = {a-b}")
    elif option == 3:
        print(f"Multiply of {a} & {b} = {a*b}")
    elif option == 4:
        print(f"Division of {a} & {b} = {a/b}")
    else:
        print("please choose right option.")
# ================================================
'''
while True: 
    print("======= Calculator =======")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit\n")
    option = int(input("Enter choice: "))
    if option == 0:
        print("Program terminated.")
        break
    else:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))
        if option == 1:
            print(f"Sum of {a} & {b} = {a+b}")
        elif option == 2:
            print(f"Difference of {a} & {b} = {a-b}")
        elif option == 3:
            print(f"Multiply of {a} & {b} = {a*b}")
        elif option == 4:
            print(f"Division of {a} & {b} = {a/b}")
        else:
            print("please choose right option.") 
'''
# ==========================================================
'''
while True: 
    print("======= Calculator =======")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit\n")
    option = int(input("Enter choice: "))
    if option == 0:
        print("Program terminated.")
        break
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    match option:
        case 1:
            print(f"Sum of {a} & {b} = {a+b}")
        case 2:
            print(f"Difference of {a} & {b} = {a-b}")
        case 3:
            print(f"Multiply of {a} & {b} = {a*b}")
        case 4:
            print(f"Division of {a} & {b} = {a/b}")
        case _:
            print("Please choose right option.")
            '''