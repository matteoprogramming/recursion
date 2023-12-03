# Exercises about recursion

# Exercise 2


# Write a recursive function that converts an integer to a string in any base. 

def convert_rec(n, base):
    figures = "0123456789ABCDEF"
    if n<base:
        return figures[n]
    else:
        return "".join((convert_rec(n//base, base), figures[n%base]))
    

if __name__ == "__main__":
    n = int(input("Enter the number you want to convert: "))
    for i in range(2,17):
        print(f"Convert {n} in base {i}\t", convert_rec(n, i))