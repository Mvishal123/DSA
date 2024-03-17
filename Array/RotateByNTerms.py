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






ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = 3

# print(brute_force(ls, d))

# optimal_solution(0, d-1, ls)
# optimal_solution(d, len(ls) - 1, ls)
# # optimal_solution(0, len(ls) - 1, ls)

# In-built-reverse
# ls[:d] = ls[:d][::-1]
# ls[d:] = ls[d:][::-1]
# ls.reverse()
#
# print(ls)