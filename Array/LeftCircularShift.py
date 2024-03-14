def first_method(ls):
    index = len(ls) - 1
    temp = ls[index]
    while index >= -1:
        replace = ls[index]
        if not index == len(ls) - 1:
            ls[index] = temp
            temp = replace

        index -= 1

    return ls

def second_method(ls):
    first = ls[0]

    index = 1
    while index < len(ls):
        ls[index - 1] = ls[index]
        index += 1

    ls[index - 1] = first

    return ls


ls = [1, 2, 3, 4, 5]
print(second_method(ls))