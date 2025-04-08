# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when you read, write, or delete attributes
#             Gives you a getter, setter, and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width} cm"

    @property
    def height(self):
        return f"{self._height} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

    
rect1 = Rectangle(32, 45)

rect1.width = 5
rect1.height = 7

# del rect1.width
# del rect1.height


print(rect1.width)
print(rect1.height)