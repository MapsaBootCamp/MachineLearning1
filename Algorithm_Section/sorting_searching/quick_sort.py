def quick_sort(arr: list) -> list:
    left, right = [], []
    if len(arr) > 1:
        pivot = arr.pop(0)
        for elm in arr:
            if elm > pivot:
                right.append(elm)
            else:
                left.append(elm)
        left = quick_sort(left)
        right = quick_sort(right)

        return left + [pivot] + right

    return arr


print(quick_sort([2, -2, 0]))
