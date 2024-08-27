#write a function to calculate the sum of min value in each row of a 2D list
def sum_of_min_values(lst):
    res = 0
    for i in range(0, len(lst)):
        res += min(lst[i])
        i += 1
    return res