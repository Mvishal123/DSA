ls = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# max number of zeros that can be flipped
k = 2

def method_1():

    max_len = 0

    for i in range(len(ls)):
        zero_count = 0
        count = 0
        for j in range(i, len(ls)):
            if ls[j] == 0:
                zero_count += 1
            if zero_count > k:
                break
            else:
                count += 1

        max_len = max(max_len, count)
        print(max_len)


def method2():
    l = 0
    r = 0
    zero_count = 0
    max_len = 0
    count = 0

    while r < len(ls):
        l = 0
        r = 0
        count = 0
        zero_count = 0
        max_len = 0
        ans = []

        while r < len(ls):
            if ls[r] == 0:
                zero_count += 1

            while zero_count > k and l <= r:
                if ls[l] == 0:
                    zero_count -= 1
                l += 1

            count = r - l + 1
            if max_len <= count:
                ans.append(ls[l: r + 1])
            max_len = max(max_len, count)

            r += 1

        print(max_len)
        print(ans)


def method3():
    l = 0
    r = 0
    count = 0
    zero_count = 0
    max_len = 0
    ans = []
    while r < len(ls):
        if ls[r] == 0:
            zero_count += 1

        if zero_count > k:
            if ls[l] == 0:
                zero_count -= 1
            l += 1

        count = r - l + 1

        ans.append(ls[l: r + 1])
        if zero_count <= k:
            max_len = max(max_len, count)
        r += 1


    print(max_len)
    print(ans)













# method_1()
# method2()
method3()