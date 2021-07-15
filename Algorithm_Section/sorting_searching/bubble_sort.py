def buuble_sort(arr: list) -> list:

    arr_size = len(arr)

    for i in range(arr_size):
        for j in range(arr_size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(buuble_sort([5, 6, -2, 0, 98, 12]))
