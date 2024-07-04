ls = [1, 2, 0, 0, 0, 1, 2]
k = 3

store = dict()

_sum = 0
_len = 0

for i in range(len(ls)):
    number = ls[i]
    _sum += number

    if not store.get(_sum):
        store[_sum] = i

    if _sum <= k:
        if _sum == k:
            _len = i + 1

    else:
        prev = _sum - k
        if prev in store.keys():
            prev_index = store[prev]
            new_len = i - prev_index

            if new_len > _len:
                _len = new_len


print(_len)