size = int(input("Enter the size of the pattern: "))
if size <= 0:
    print("Please enter a positive integer.")
current_row = 1
while current_row <= size:
    for colum in range(size):
        print("*", end="")
    print()
    current_row += 1
    print()


