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
    l, r = 0, 0
    _len = 0
    store = dict()

    while r < len(ls):
        if store.get(ls[r]) and r > store.get(ls[r]) >= l:
            l = store.get(ls[r]) + 1

        _len = max(_len, r - l + 1)
        store[ls[r]] = r

        print(store)
        r += 1

    print(_len)







# method_1()
method_2()

