ls = [2, 4, 1, 7, 10]
k = 14

# Sum -lte k
max_len = 0
for i in range(len(ls)):
    _sum = 0
    for j in range(i, len(ls)):
        _sum += ls[j]

        if _sum > k:
            break
        else:
            max_len = max(max_len, j - i + 1)

print(max_len)

def get_all_sub_arrays():
    for i in range(len(ls)):
        for j in range(i, len(ls)):
            print(ls[i:j + 1])

        print("------------------")

# get_all_sub_arrays()
