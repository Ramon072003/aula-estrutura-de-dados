array = [2,5,8,3,-2,9,0]
targetSum = 3

for i in range(0, len(array)):
    for j in range(0, len(array)):
        if array[i] + array[j] == targetSum:
            print(f"Its here! {array[i]} + {array[j]} = {array[i]+array[j]}")
