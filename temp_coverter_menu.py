while True:
    temperature=int(input("enter temperature:"))
    print("\n1.\tConvert Celsius to Fahrenheit\n"
          "2.\tConvert Fahrenheit to Celsius\n3.\tExit the program\n")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        f=(9/5*temperature)+32
        print(f"{temperature} celsius is {f} fahrenheit")
    elif choice==2:
        c=5/9*(temperature-32)
        print(f"{temperature} fahrenheit is {c} celsius")
    elif choice==3:
        break
    else:
        print("Invalid Entry")


