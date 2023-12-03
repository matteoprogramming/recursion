# Exercises about recursion

# Exercise 5


# Write a recursive function that computes
# the nth term of the Fibonacci sequence

def fib_rec(n):
    if n in {1,2}:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)
    
if __name__ == "__main__":
    n = int(input("Enter the a number: "))
    print(f"The {n}th term of the Fibonacci's sequence is: {fib_rec(n)}")