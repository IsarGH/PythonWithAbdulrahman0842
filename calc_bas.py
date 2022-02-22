
num1 = int(input("Enter Value:"))
num2 = int(input("Enter Value:"))
opr = input("Which Operation do you want to perform?( '+' , '-' , '*' , '/' )\n")
if opr=="+":
    sum = num1+num2
    print(num1 , "+",num2 ,"=" ,sum)
elif opr=="-":
    sub = num1-num2
    print(num1, "-", num2, "=", sub)
elif opr=="*":
    mult=num1*num2
    print(num1, "*", num2, "=", mult)
elif opr=="/":
    divs=num1/num2
    print(num1, "/", num2, "=", divs)
else:
    print("error")
