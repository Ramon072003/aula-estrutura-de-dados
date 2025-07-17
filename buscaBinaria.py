def lomuto(array, inicio, fim):
    pivo = array[fim]
    i = inicio-1
    for j in range(inicio, fim):
        if array[j] <= pivo:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[fim] = array[fim], array[i+1]
    return i+1

def quickSort(array, left, right):
    if left < right:
        pivo = lomuto(array, left, right)
        quickSort(array, left, pivo-1)
        quickSort(array, pivo+1, right)
        return array
    
def binary_search(array, value):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


array = [55,10,211,43,4,5,8]
ordened_array = quickSort(array, 0, len(array)-1)
print(ordened_array)
print(binary_search(ordened_array, 8))
