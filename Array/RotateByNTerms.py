# T.C => O(d) + (N-d) + O(d) => O(N+d)
# S.C => O(d)
def brute_force_left(ls, d):
    temp = []
    for i in range(d):
        temp.append(ls[i])

    for i in range(d, len(ls)):
        ls[i - d] = ls[i]

    for i in range(len(temp)):
        ls[len(ls) - (d - i)] = temp[i]

    return ls

# T.C = O(d) + o(N-d) + O(N) => O(2N)
# S.C = O(1)
def optimal_solution_left(s, e, ls):
    while s < e:
        temp = ls[s]
        ls[s] = ls[e]
        ls[e] = temp

        s+=1
        e-=1



# T.C = O(d) + O(N-d) + O(d) => O(N+d)
# S.C = O(d)
def brute_force_right(ls):
    temp = ls[len(ls) - d:]
    for i in range(len(ls)-1, d-1, -1):
        ls[i] = ls[i - d]
        # ls[i+d] = ls[i]

    ls = temp + ls[d:]

    return ls

def optimal_right(ls, d):
    # for i in range(len(ls)-1, len(ls)-d, -1):
    ls[len(ls)-d:] = ls[len(ls)-d:][::-1]
    ls[:len(ls)-d] = ls[:len(ls)-d][::-1]
    ls.reverse()

    return ls

def optimal_left_slicing(ls, d):
    ls[:d] = ls[:d][::-1]
    ls[d:] = ls[d:][::-1]
    ls.reverse()
    return ls






ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = 2

# print(ls[len(ls) - d: ])
# print(brute_force_right(ls))
# print(brute_force(ls, d))
print(optimal_right(ls1, d), "right")
print(optimal_left_slicing(ls2, d), "left")

# for i in range(len(ls) -1, d-1, -1):
#     print(i)


# In-built-reverse
# ls[:d] = ls[:d][::-1]
# ls[d:] = ls[d:][::-1]
# ls.reverse()
# print(ls)

