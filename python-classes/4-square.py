class Square:
    def __init__(self, size=0):
        self.__size = size  # Initialize private attribute

    @property
    def size(self):
        return self.__size  # Getter for size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Setter with validation

    def area(self):
        return self.__size**2

    def __str__(self):
        return f"Square with size: {self.__size}"

    def __repr__(self):
        return f"Square({self.__size})"

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

