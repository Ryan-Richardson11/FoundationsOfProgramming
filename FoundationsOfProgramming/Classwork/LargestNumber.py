def main():
    a = eval(input("Enter your first number (a): "))
    b = eval(input("Enter your first number (b): "))
    c = eval(input("Enter your first number (c): "))

    if (a>b):
        if (a>c):
            print("The largest is", a)
        else:
            print("The largest is", c)
    else:
        if (b>c):
            print("The largest is", b)
        else:
            print("The largest is", c)
main()
            
