# t = 5
# ls = [1, 2, 1, 3, 2, 1]
#
# hashArr = [0 for i in range(13 + 1)]
#
# for i in ls:
#     hashArr[i] += 1
#
# n = [2, 3, 4, 1]  
#
# for i in n:
#     print(f"Count of {i}: {hashArr[i]}")


# ch = "asdasfaevciaez"
# hashCh = [0 for i in range(25 + 1)]
#
# for i in ch:
#     hashCh[ord(i) - 97] += 1
#
#
# for i in range(26):
#     print(f"Count of {chr(97 + i)} = {hashCh[i]}")

# ls = [12, 1, 2, 3, 2, 2, 1, 2, 3, 12]
#
# store = dict()
#
# for i in ls:
#     store[i] = store.get(i, 0) + 1
#
# for i in store.keys():
#     print(i)
#
# print(store)

# set is ordered
# myset = {5, 3, 4, 2, 1}
# fset = frozenset({5, 1, 2, 3, 4, 5, 1})
# tup = (5, 3, 2, 1, 3, 1 )
#
#
# myset.add(12)
# print(myset)
# print(fset)
# print(tup)

ls = [5,10,10,5,10,15,10,5]

store = dict()

for i in ls:
    store[i] = store.get(i, 0) + 1

print(store)
firstMax = -1
secondMax = -1

for key, value in store.items():
    if value > firstMax:
        secondMax = firstMax
        firstMax = key
    else:
        if value > secondMax:
            secondMax = key

print(firstMax, secondMax)