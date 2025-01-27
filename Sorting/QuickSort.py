def pivotSort(arr, low, high):
    pivot = low

    while low < high:
        while arr[low] <= arr[pivot]:
            low += 1

        while arr[high] > arr[pivot]:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[pivot], arr[high] = arr[high], arr[pivot]
    return low


def qSort(arr, low, high):
    if low >= high:
        return

    pivotIndex = pivotSort(arr, low, high)

    qSort(arr, low, pivotIndex - 1)
    qSort(arr, pivotIndex +1, high)


ls = [5, 3, 2, 12, 4]
print(ls)
qSort(ls, 0, len(ls) - 1)
print(ls)
