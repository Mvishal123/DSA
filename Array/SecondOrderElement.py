# Problem Statement: Given an array, find the second smallest and second largest element in the array.
# Print ‘-1’ in the event that either of them doesn’t exist.

def findSecondSmallest(ls):
    smallest = ls[0]
    sSmallest = 100000

    for n in range(len(ls)):
        if ls[n] < smallest:
            sSmallest = smallest
            smallest = ls[n]

        else:
            if ls[n] < sSmallest and ls[n] != smallest:
                sSmallest = ls[n]

    return sSmallest


def findSecondLargest(ls):
    largest = ls[0]
    sLargest = -100000

    for i in range(len(ls)):
        if ls[i] > largest:
            sLargest = largest
            largest = ls[i]

        else:
            if(ls[i] > sLargest) and ls[i] != largest:
                sLargest = ls[i]

    return sLargest


ls = [10, 6, 7, 5, 4, 1, 2, 22, 2]


print(findSecondSmallest(ls))
print(findSecondLargest(ls))