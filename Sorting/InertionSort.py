def swap(arr, f, s):
    temp = arr[f]
    arr[f] = arr[s]
    arr[s] = temp


def insertionSort(arr):
    for i in range(len(arr) - 1):
        idx = i + 1
        while idx > 0:
            if arr[idx] < arr[idx - 1]:
                swap(arr, idx, idx - 1)
            idx -= 1


ls = [4, 3, 5, 1, 2]
insertionSort(ls)

print(ls)