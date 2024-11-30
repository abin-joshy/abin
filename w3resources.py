def maximum():
    numbers = []
    print("Enter three numbers")
    for i in range(3):
        number = int(input('enter the numbers:'))
        numbers.append(number)
    print("The largest number among the three number is:", max(numbers))
maximum()
def add_list(list1):
    print("The sum of the list of numbers is:",sum(list1))
add_list([3,6,7])
def multiply(list1):
    product=1
    for i in list1:
        product*=i
    print("The product of the list of numbers is:",product)
multiply([5,7,2,3])
def reverse_string(str1):
    length=len(str1)
    print("The reversed string is:",str1[length::-1])
reverse_string("abcd1234")
def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    print("The factorial of",number,"is:",fact)
factorial(6)




