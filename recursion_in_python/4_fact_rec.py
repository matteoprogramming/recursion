# Exercises about recursion

# Exercise 4


# Write a function that computes the factorial of a natural number.

def fact_rec(n):
    if n in {0, 1}:
        return 1
    else:
        return n * fact_rec(n-1)

print(fact_rec(56))