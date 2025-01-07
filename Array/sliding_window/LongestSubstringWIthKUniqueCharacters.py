s = "aaabbccd"
k = 2

store = dict()
_max = 0

l = r = 0

while r < len(s):
    rChar = s[r]
    lChar = s[l]

    store[rChar] = store[rChar] + 1 if store.get(rChar) else 1

    if len(store) > k:
        if store.get(lChar) >= 2:
            store[lChar] -= 1
        else:
            del store[lChar]

        l += 1

    _max = max(_max, r - l + 1)
    r += 1

print(_max)