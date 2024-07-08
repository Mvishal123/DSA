ls = 'cadbzabcd'

# T.C = O(n^2)
# S.C = O(n)
def method_1():
    _max_len = 0
    for i in range(len(ls)):
        _dict = {}
        for j in range(i, len(ls)):
            if _dict.get(ls[j]):
                _max_len = max(_max_len, j - i)
                break

            _dict[ls[j]] = 1
        print(_dict)



    print(_max_len)


def method_2():
    l = 0
    r = 0
    max_len = 0
    store = {}

    while r < len(ls):
        if l != r and store.get(ls[r]) !=         while not store.get(ls[r]) and l <= r:
            store[ls[r]] = 1

        max_len = max(max_len, r - l + 1)





method_1()

