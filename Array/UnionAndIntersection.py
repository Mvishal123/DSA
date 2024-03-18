arr1 = [1, 1, 2, 3, 8, 9, 10]
arr2 = [2, 8]

# Output
# condition -> arrays should be sorted
# union -> [1, 2, 3, 4, 5, 6, 7]
# intersection -> [3, 5]


def inbuilt(arr1, arr2):
    print(set(arr1).intersection(arr2))


def union_method_1(ls1, ls2):
    final = []
    last = -10000
    i, j = 0, 0

    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            if ls1[i] != last:
                final.append(ls1[i])
                last = ls1[i]
            i+=1
        else:
            if ls2[j] != last:
                final.append(ls2[j])
                last = ls2[j]
            j+=1

    while i < len(ls1):
        if ls1[i] != last:
            final.append(ls1[i])
            last = ls1[i]
        i+=1

    while j < len(ls2):
        if ls2[j] != last:
            final.append(ls2[j])
            last = ls2[j]
        j+=1

    return final


def intersection_method_1(ls1, ls2):
    last = -10000
    final = []
    if len(ls1) > len(ls2):
        for i in ls1:
            for j in ls2:
                if i == j:
                    if j != last:
                        final.append(i)
                        last = j
    else:
        for i in ls2:
            for j in ls1:
                if j == i:
                    if j != last:
                        final.append(i)
                        last = i
    return final


def intersection_optimal_method(ls1, ls2):
    # check which arr is less in size and start with it, but we won't be doing that here.

    final = []
    i, j = 0, 0

    while i < len(ls1) and j < len(ls2):
        # As the array is sorted no need to check the other elements also
        if ls1[i] < ls2[j]:
            i+=1
        elif ls1[i] > ls2[j]:
            j+=1
        else:
            final.append(ls1[i])
            i+=1
            j+=1
    return final






print(union_method_1(arr1, arr2))
# print(intersection_method_1(arr1, arr2))
print(intersection_optimal_method(arr1, arr2))
# s1 = set(arr1).union(arr2)
# s2 = set(arr1).intersection(arr2)
# ls1 = []
# l2 = []
#
# print(list(s1))
# print(list(s2))


