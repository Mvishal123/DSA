def printNTimes(n):
    if n == 0:
        return
    printNTimes(n - 1)
    print("Vishal", n)


def printOneToN(n):
    if n == 0:
        return
    printOneToN(n - 1)
    print(n)


def sum_of_n_numbers(n, sum=0):
    if n == 0:
        print("SUM:", sum)
        return

    sum += n
    sum_of_n_numbers(n - 1, sum)


def factorial(n, fact=1):
    if n <= 1:
        print("FACTORIAL:", fact)
        return

    factorial(n - 1, fact * n)


def reverse_array(arr, f=0, l=0):
    if f == l:
        print("REVERSED_ARR:", arr)
        return

    arr[f], arr[l] = arr[l], arr[f]
    reverse_array(arr, f + 1, l - 1)


def palindrome_cheker(s, f, l):
    if l == f:
        print("IS PALINDROME:", True)
        return

    if s[f] != s[l]:
        print("IS PALINDROME:", False)
        return

    palindrome_cheker(s, f + 1, l - 1)


def fibo(n, ans=0):
    pass







# printNTimes(10)
# printOneToN(10)
# sum_of_n_numbers(10)
# factorial(8)
# reverse_array([1, 2, 3, 4, 5], 0, 5 - 1)
s = "MADAM"
# palindrome_cheker("MADAM", 0, len(s) - 1)
fibo(5)