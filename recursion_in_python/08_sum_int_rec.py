# Exercises about recursion

# Exercise 8


# Write a function that takes an integer and
# returns the sum of the first n integers.

def sum_int_rec(n):
    if n == 1:
        return 1
    else:
        return n + sum_int_rec(n-1)
    
def sum_int(n):
    return n*(n+1)//2

if __name__ == "__main__":
    n = int(input("Enter the number of the first natural numbers that you want to sum: "))
    print(f"Sum of the first {n} natural numbers: {sum_int_rec(n)}\t(expected {sum_int(n)})")