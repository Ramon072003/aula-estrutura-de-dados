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


def two_sums(array, target_sum):
    new_array= quickSort(array, 0, len(array)-1)
    left = 0
    right = len(new_array)-1
    while left < right:
        sum = new_array[left] + new_array[right]
        if sum == target_sum:
            return (array[left], array[right])
        elif sum < target_sum:
            left +=1
        else:
            right -=1
    return None

array = [5,2,3]
response = two_sums(array, 8)
print(response)