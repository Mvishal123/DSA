s = "aaacb"

_count = 0
for i in range(len(s)):
    _set = set()
    for j in range(i, len(s)):
        _set.add(s[j])

        if len(_set) >= 3:
            _count += len(s) - j
            break

print(_count)
