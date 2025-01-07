fruits = [0, 0, 0, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1]

store = dict()

for i in fruits:
    store[i]  = store.get(i) + 1 if i in store else 1


print(store)