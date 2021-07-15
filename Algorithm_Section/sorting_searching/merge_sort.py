def merge_sort(arr: list) -> list:
    middle = len(arr) // 2

    if len(arr) > 1:
        left = arr[:middle]
        right = arr[middle:]

        print("left: ", left)
        print("right: ", right)

        left = merge_sort(left)
        right = merge_sort(right)

        arr = []
        while left and right:
            if left[0] < right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)

        arr.extend(left)
        arr.extend(right)

        print("after merge: ", arr)

    return arr


print(merge_sort([1, -2, 8]))
