fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]


def method_1():
    store = dict()
    count = 0
    l = 0
    r = 0
    _max = 0
    ans = list()

    while r < len(fruits):
        store[fruits[r]] = store.get(fruits[r], 0) + 1
        # print(store)

        while len(store) > 2 and l <= r:
            item = fruits[l]
            store[item] -= 1

            if store[item] == 0:
                del store[item]

            l += 1

        count = r - l + 1
        if _max < count:
            ans.append(fruits[l: r + 1])
        _max = max(_max, count)
        r += 1

    print(store)
    print(_max)
    print(ans)


def method_2():
    l = 0
    r = 0
    _max = 0
    count = 0
    store = dict()
    ans = []

    while r < len(fruits):
        store[fruits[r]] = store.get(fruits[r], 0) + 1

        if len(store) > 2:
            store[fruits[l]] -= 1

            if store[fruits[l]] == 0:
                del store[fruits[l]]

            l += 1

        count = r - l + 1
        if _max < count:
            ans.append(fruits[l: r + 1])
        _max = max(_max, count)

        r += 1


    print(_max)
    print(ans)


# method_1()
method_2()
