# Exercises about recursion

# Exercise 6


# Write a recursive function that returns the first n terms
# of the Fibonacci sequence


def fibonacci_sequence_rec(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        sequence = fibonacci_sequence_rec(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of first terms of the Fibonacci sequence you want: "))
    l  = fibonacci_sequence_rec(n)
    print(f"The first {n} terms in the Fibonacci sequence are:\n")
    for i, el in enumerate(l):
        print(f"{i+1})\t{el}")
