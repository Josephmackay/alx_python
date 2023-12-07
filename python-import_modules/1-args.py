import sys

number_of_arguments = len(sys.argv)

if number_of_arguments == 1:
    print("Number of argument(s): 0.")
else:
    print(f"Number of argument{'s' if number_of_arguments > 1 else ''}: {number_of_arguments}.")

    for i, argument in enumerate(sys.argv[1:]):
        print(f"{i + 1}: {argument}")
if __name__ == "__main__":
    pass        