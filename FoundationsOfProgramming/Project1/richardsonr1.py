#importing a math module in order to complete the calculations
import math
#the user will enter their radius here
user_radius = float(input("Type your radius: "))
#Calculation of area preformed
area = math.pi * user_radius * user_radius
#Calculation of circumference preformed
circumference = 2 * math.pi * user_radius
#Calculation of volume preformed
volume = 4/3 * math.pi * user_radius**3
#Each calculation is printed with it's correlated string
print("The area is: ", area)
print("The circumference is: ", circumference)
print("The volume is: ", volume)
