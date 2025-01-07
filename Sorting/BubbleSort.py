def swap(arr, f, s):
    temp = arr[f]
    arr[f] = arr[s]
    arr[s] = temp


def bubbleSort(arr):
    for i in range(len(arr)):
        isSwapped = False
        for idx in range(len(arr) - i - 1):
            if arr[idx + 1] < arr[idx]:
                isSwapped = True
                swap(arr, idx, idx + 1)

        if not isSwapped:
            return


ls = [3, 1, 5, 4, 2]
bubbleSort(ls)

print(ls)