def check_odd(num):
    if num%2!=0:
        return "odd"
    else:
        return "not odd"
    num=int(input("enter sa number: "))
    print(check_odd(num))