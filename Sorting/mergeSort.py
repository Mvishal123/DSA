def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    first = merge_sort(arr[:mid])
    second = merge_sort(arr[mid:])

    merged_arr = [1 for i in range(len(first) + len(second))]

    p1 = 0
    p2 = 0
    index = 0

    while p1 < len(first) and p2 < len(second):
        if first[p1] < second[p2]:
            merged_arr[index] = first[p1]
            p1 += 1
        else:
            merged_arr[index] = second[p2]
            p2 += 1

        index += 1

    while p1 < len(first):
        merged_arr[index] = first[p1]
        p1 += 1
        index += 1

    while p2 < len(second):
        merged_arr[index] = second[p2]
        p2 += 1
        index += 1

    return merged_arr


def merge(arr, low, mid, high):
    f = low
    s = mid + 1
    temp = []
    index = 0

    while f <= mid and s <= high:
        if arr[f] < arr[s]:
            temp.append(arr[f])
            f += 1
        else:
            temp.append(arr[s])
            s += 1
        index += 1

    while f <= mid:
        temp.append(arr[f])
        f += 1
        index += 1

    while s <= high:
        temp.append(arr[s])
        s += 1
        index += 1

    idx = 0
    for i in range(low, high + 1):
        arr[i] = temp[idx]
        idx += 1


def merge_sort_space_optimised(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort_space_optimised(arr, low, mid)
    merge_sort_space_optimised(arr, mid + 1, high)

    merge(arr, low, mid, high)


ls = [5, 4, 3, 2, 1, 5, -10]

# merged = merge_sort(ls)
merge_sort_space_optimised(ls, 0, len(ls) - 1)
print(ls)
