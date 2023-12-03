# Exercises about recursion

# Exercise 11


# Write a recursive function that performs exponentiation.


def pow_rec(a, b):
    if b == 0:
        return 1
    else:
        return a*pow_rec(a, b-1)


if __name__ == "__main__":
    print("Enter two numbers to exponentiate.")
    a = int(input("1) Base -->\t"))
    b = int(input("2) Exponent -->\t"))
    print(f"The recursive pow made between {a} and {b} gives: {pow_rec(a,b)}\t\t (expected {(a**b)})")