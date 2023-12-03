# Exercises about recursion

# Exercise 1


# Write a  recursive function that computes the sum of a list of numbers. 

def sum_rec(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0]+sum_rec(l[1:])
    

if __name__ == "__main__":
    l = [[0, 774, 855, 7, 45, 99], [54, 74, 85, 85, 74, 44], [78, 56, 445655, 8554, 7485]]
    for i, el in enumerate(l):
        print("\nConsider\t",l[i])
        print("recursive sum\t", sum_rec(l[i]))
        print("expected sum\t", sum(l[i]), end="\n\n")
