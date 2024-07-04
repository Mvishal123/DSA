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


ls = [1, 2, 3, 1, 2, 1]
k = 4

stats = {
    "first": 0,
    "last": 0,
    "size": 0
}

length = len(ls)

for i in range(length):
    _sum = 0
    _count = 0
    for j in range(i, length):
        _sum += ls[j]
        _count += 1

        if _sum == k and _count > stats["size"]:
            stats["size"] = _count
            stats["first"] = i
            stats["last"] = j
            break

        elif _sum > k:
            break

print(stats)
print(ls[stats["first"]: stats["last"] +1 ])



print(number_of_sub_arrays(arr, 3))
print(longest_sub_array(arr, 3))





def optimal_two_pointer_approach(arr, k):
    _sum = 0
    _len = 0

    left = 0
    right = 0

    length = len(arr)

    while right < length:
        _sum += arr[right]

        while left <= right and _sum > k:
            _sum -= arr[left]
            left += 1

        if _sum == k:
            new_len = right - left + 1
            _len = max(_len, new_len)

        right += 1

    print(_len)

arr = [1,2,1,2,1]
k = 3

optimal_two_pointer_approach(arr, k)






















