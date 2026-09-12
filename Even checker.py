def check_even(num):
    if num%2==0:
        return "even"
    else:
        return "not even"

num=int(input("Enter a number: "))
print(check_even(num))
