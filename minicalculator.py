first = input("enter the first number ") 

operetor = input("enter the operator (+, -, *, /, % ) " )

second = input("enter the second number ")

first = int(first)
second = int(second)

if operetor == "+" :
    print(first + second )   

elif operetor == "-" :
    print(first - second )   

elif operetor == "*" :
    print(first * second )   

elif operetor == "/" :
    print(first / second )   

elif operetor == "%" :
    print(first % second )   

else :
    print("invalid operator")
