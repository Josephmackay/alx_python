class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        return self.__size

    def area(self):
        return self.__size**2

    def perimeter(self):
        return 4 * self.__size

    def __str__(self):
        return f"Square with size: {self.__size}"

    def __repr__(self):
        return f"Square({self.__size})"