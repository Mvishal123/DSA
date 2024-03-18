ls = [0, 1, 3, 2]


# T.C -> O(N) * O(N)
# S.C -> O(1)
def brute_force(ls):
    for i in range(len(ls) + 1):
        flag = False
        for j in ls:
            if j == i:
                flag = True
                break

        if not flag:
            return i
        flag = False


# T.C -> O(N) + O(N+1) => O(2N)
# S.C -> O(N)
# Using an hash array
def better_approach(ls):
    temp = [0 for i in range(len(ls) + 1)]

    for i in ls:
        temp[i] = 1

    for i in range(len(temp)):
        if temp[i] == 0:
            return i


# This problem has 2 optimal solutions
# Sum and XOR

# SUM method
# T.C -> O(N)
# S.C -> O(1)
def optimal_sum_method(ls):
    N = len(ls)
    sumLs = (N*(N+1))//2

    for i in ls:
        sumLs -= i

    return sumLs

# XOR
def optimal_xor_method(ls):
    pass
#     learn later


print(brute_force(ls))
print(better_approach(ls))
print(optimal_sum_method(ls))
print(optimal_xor_method(ls))
