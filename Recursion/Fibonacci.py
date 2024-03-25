def fibo(N):
    # Base condition
    if N < 2:
        return N

    return fibo(N-1) + fibo(N-2)


print(fibo(5))
