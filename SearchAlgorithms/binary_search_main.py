def binary_search(arr, target):
    s = 0
    e = len(arr) - 1

    while s < e:
        mid = int((s + e) / 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1

    return -1


ls = [2, 4, 5, 7, 12, 14, 15, 19]
print(binary_search(ls ,8))

