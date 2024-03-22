arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
k = 3

def number_of_sub_arrays(ls, k):
    count = 0

    for i in range(len(ls)):

        sum = 0
        for j in range(i, len(ls)):
            sum += ls[j]
            if sum > k:
                break
            if sum == k:
                count+=1
                break

    return count

def longest_sub_array(ls, k):
    maxLen = 0
    for i in range(len(ls)):
        l = 0
        sum = 0

        for j in range(i, len(ls)):
            sum += ls[j]
            l += 1

            if sum > k:
                break

            if sum == k:
                maxLen = max(maxLen, l)

    return maxLen



print(number_of_sub_arrays(arr, 3))
print(longest_sub_array(arr, 3))