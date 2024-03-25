def printWordNTimes(string, N):
    if N <= 0:
        return
    else:
        print(string)
        N-=1
        printWordNTimes(string, N)


printWordNTimes("hello", 10)