# Exercises about recursion

# Exercise 9


# Write a function that takes a positive integer
# as input and returns the harmonic sum up to n.


def harmonic_sum_rec(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum_rec(n-1)
    


if __name__ == "__main__":
    n = int(input("Enter the term up to which you want to calculate the harmonic sum: "))
    print("Result: ", harmonic_sum_rec(n))