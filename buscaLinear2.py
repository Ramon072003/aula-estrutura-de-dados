def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


array = [55,10,211,43,4,5,8]
print(linear_search(array, 18))
