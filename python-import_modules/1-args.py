import sys

number_of_arguments = len(sys.argv)

if number_of_arguments == 1:
    print("0 arguments.")
elif number_of_arguments == 2:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
elif number_of_arguments == 3:
    print("2 arguments:")
    print("1: {}".format(sys.argv[1]))
    print("2: {}".format(sys.argv[2]))
elif number_of_arguments == 4:
    print("3 arguments:")
    print("1: {}".format(sys.argv[1]))
    print("2: {}".format(sys.argv[2]))
    print("3: {}".format(sys.argv[3]))
elif number_of_arguments == 5:
    print("4 arguments:")
    print("1: {}".format(sys.argv[1]))
    print("2: {}".format(sys.argv[2]))
    print("3: {}".format(sys.argv[3]))
    print("4: {}".format(sys.argv[4]))
else:
    print("Unexpected number of arguments: {}".format(number_of_arguments))
if __name__ == "__main__":
    pass        