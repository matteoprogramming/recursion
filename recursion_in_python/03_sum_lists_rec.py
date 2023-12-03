# Exercises about recursion

# Exercise 3


# Write a function that sums recursion lists.
# Ex: [1, 2, [3,4], [5,6]] --> 21

def sum_lists_rec(l):
    s = 0
    for el in l:
        if type(el) == list:
            s += sum_lists_rec(el)
        elif type(el) == int:
            s += el
    else:
        return s

if __name__ == "__main__":
    print(sum_lists_rec([1, 2, [3,4], [5,6]]))
    print(sum_lists_rec([6, 2, [78, [75, [25]]], [3,4], [5, 9, [78, 74, [[[5]]]],6]]))