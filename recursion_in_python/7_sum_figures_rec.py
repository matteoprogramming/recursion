# Exercises about recursion

# Exercise 7


# Write a recursive function that takes as input an integer
# and returns the sum of its figures.

def sum_figures_rec(n):
    if n<10:
        return n
    else:
        return n%10 + sum_figures_rec(n//10)
    
if __name__ == "__main__":
    numbers = [78, 85, 9654, 7542, 48, 74]
    for n in numbers:
        print(f"The sum of the figures of\t{n}\t is\t {sum_figures_rec(n)}")