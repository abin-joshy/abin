temperature=int(input("enter temperature:"))
scale=input("Is this in (C)elsius or (F)ahrenheit?:")
if scale=='c' or scale=="C"                                              =='C':
    f=(9/5*temperature)+32
    print(temperature,"Celsius is",f,"Fahrenheit.")
if scale=='f' or scale=='F':
    c=5/9*(temperature-32)
    print(temperature,"Fahrenheit is",c,"Celsius.")
