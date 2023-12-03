# Exercises about recursion

# Exercise 10


# Wwrite a recursive function that sums
# two numbers given as input.


def add_rec(a, b):
    if b == 0:
        return a
    else:
        return add_rec(a, b-1) + 1
    


if __name__ == "__main__":
    print("Enter the two numbers you want to add")
    a = int(input("1) -->\t"))
    b = int(input("2) -->\t"))
    print(f"The recursive sum made between {a} and {b} gives: {add_rec(a,b)}\t\t (expeted {(a+b)})")