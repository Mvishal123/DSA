def swap(arr, f, s):
    temp = arr[f]
    arr[f] = arr[s]
    arr[s] = temp


def selectionSort(arr):
    for i in range(len(ls)):
        _max = 0
        for idx in range(1, len(ls) - i):
            if arr[_max] < arr[idx]:
                _max = idx
        swap(arr, len(arr) - i - 1, _max)


ls = [4, 5, 1, 2, 3]
selectionSort(ls)
print(ls)
