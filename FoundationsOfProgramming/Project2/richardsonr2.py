#defining a main function
def main():
#creating two variables for the user to input
    a = eval(input("Enter your first positive integer: "))
    b = eval(input("Enter your second positive integer: "))
#a while loop to run until the condition is true where it will break
    while True:
        if(a%b == 0 or b%a == 0):
            print(a%b == 0 or b%a == 0)
            break
        elif(a%b != 0 or b%a != 0):
            print(False)
#calling back the variables for a new input since the condition to break was not met
            a = eval(input("Enter your first positive integer: "))
            b = eval(input("Enter your second positive integer: "))
             
#main function called
main()

