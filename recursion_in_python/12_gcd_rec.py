# Exercises about recursion

# Exercise 12


# Write a recursive function that finds the greatest common divisor (GCD) of two integers. 


def gcd_rec(a, b):
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    else:
        return gcd_rec(max(a,b)%min(a,b), min(a,b))
    

def gcd(a,b):
    n = min(a,b)
    while a%n + b%n != 0:
        n -=1
    return n



if __name__ == "__main__":
    print("Enter two numbers of which you want to calculate the greatest common divisor: ")
    a = int(input("1) -->\t"))
    b = int(input("2) -->\t"))
    print(f"The greatest common divisor between {a} and {b} is: {gcd_rec(a,b)}\t (expeted {gcd(a, b)})")