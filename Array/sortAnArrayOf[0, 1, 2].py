ls = [1, 1, 1, 2, 2, 0, 0, 1, 0, 2, 2, 1, 0]



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


bubbleSort()



