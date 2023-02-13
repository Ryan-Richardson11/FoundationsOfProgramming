"""
Rectangle class

This class stores methods for a rectangle object, including the calculation of its perimeter and area.
"""
class Rectangle:
    """
    Constructor method for the Rectangle class

    Parameters:
    width (int): width of the rectangle
    length (int): length of the rectangle
    """
    def __init__(self, width, length):
        self.width = width
        self.length = length

    """
    Perimeter method for Rectangle class

    Returns:
    int: The perimeter of the rectangle, calculated as 2 * (width + length)
    """
    def perimeter(self):
        return 2 * (self.width + self.length)

    """
    Area method for Rectangle class

    Returns:
    int: The area of the rectangle, calculated as width * length
    """
    def area(self):
        return (self.width * self.length)

    """
    Display method for Rectangle class

    Prints out the user input for width and length, as well as the calculations for perimeter and area.
    """
    def display(self):
        perimeter = self.perimeter()
        area = self.area()
        print("The width of the rectangle is {}".format(self.width))
        print("The length of the rectangle is {}".format(self.length))
        print("The perimeter of the rectangle is {}".format(perimeter))
        print("The area of the rectangle is {}".format(area))

"""
Parallelepiped class

This class is a child class of the Rectangle class and stores methods for a parallelepiped object, including calculation of its volume.
"""
class Parallelepiped(Rectangle):
    """
    Constructor method for Parallelepiped class

    Parameters:
    width (int): width of the parallelepiped
    length (int): length of the parallelepiped
    height (int): height of the parallelepiped
    """
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height

    """
    Volume method for Parallelepiped class

    Returns:
    int: The volume of the parallelepiped, calculated as width * length * height
    """
    def volume(self):
        return  self.width * self.length * self.height

    """
    Display method for Parallelepiped class

    Calls the display method from the parent class Rectangle and also prints out the height and volume of the parallelepiped.
    """
    def display(self):
        super().display()
        volume = self.volume()
        print("The height of the parallelepiped is {}".format(self.height))
        print("The volume of the parallelepiped is {}".format(volume))

"""
Main function

This function prompts the user for the width, length, and height of the parallelepiped, creates an object of the Parallelepiped class, and calls the display method to print out all calculated values.
"""
def main():

    width = int(input("Please enter the rectangle's width: "))
    length = int(input("Please enter the rectangle's length: "))
    height = int(input("Please enter the parralelepiped's height: "))

    p = Parallelepiped(width, length, height)
    p.display()

if __name__ == "__main__":
    main()