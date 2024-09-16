ls = [0, 1, 2, 0, 1, 2 ]


def swap(ls, index1, index2):
    temp = ls[index1]
    ls[index1] = ls[index2]
    ls[index2] = temp


def bubbleSort():
    for i in range(len(ls)):
        for j in range(1, len(ls) - i):
            if ls[j - 1] > ls[j]:
                swap(ls, j - 1, j)
            else:
                continue

    print(ls)


def dutchNationalFlagSort(ls):
    low = 0
    high = len(ls) - 1
    ptr = 0

    while ptr <= high:
        if ls[ptr] == 0:
            swap(ls, low, ptr)
            low += 1

        elif ls[ptr] == 2:
            swap(ls, ptr, high)
            high -= 1
            ptr -= 1
        ptr += 1
    print(ls)


# bubbleSort()
dutchNationalFlagSort(ls)


