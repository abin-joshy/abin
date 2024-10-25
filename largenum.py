number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
number3=int(input("enter the third number:"))
if number1>number2 and number1>number3:
    print("The largest number is:",number1)
elif number2>number3:
    print("The largest number is:",number2)
else:
    print("The largest number is:",number3)
