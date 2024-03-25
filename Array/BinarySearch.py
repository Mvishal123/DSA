def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    ans = [-1, -1]
    while start <= end:
        mid = int(start + (end - start)/2)
        if arr[mid] == target:
            ans = [arr[mid], mid]
            break
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return ans


ls = [1, 2, 3, 5, 6, 7, 9, 10]

# return answer as [target, index]. If not found [-1, -1]
print(binarySearch(ls, 4))

