#pattern1 -> constant window
#pattern2 -> longest subarray/substring


def sub_pattern():
    ls = [0, 0, 0, 1, 2, -1, 1]
    lists = []
    k = 3
    left = 0
    right = 0
    max_len = 0
    _sum = 0

    while right < len(ls):
        _sum += ls[right]


        while _sum > k and left <= right:
            _sum -= ls[left]
            left += 1

        if _sum == k:
            lists.append(ls[left: right+1])
            max_len = max(max_len, right - left + 1)

        right += 1

    print(max_len)
    print(lists)


# sub_pattern()


