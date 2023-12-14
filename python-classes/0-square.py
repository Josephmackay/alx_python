class Square:
    def __init__(self, size):
        self.__size = size

    def size(self, new_size):
        if isinstance(new_size, int) and new_size > 0:
            self.__size = new_size

    ...
