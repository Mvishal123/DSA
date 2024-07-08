ls = [1, 2, 3, 4, 6]
k = 4

lSum = 0
rSum = 0
maxSum = 0

for i in range(k):
    lSum += ls[i]
    maxSum = max(maxSum, lSum)

left = k - 1
right = len(ls) - 1
for i in range(k):
    lSum -= ls[left]
    left -= 1
    rSum += ls[right]
    right -= 1

    maxSum = max(maxSum, lSum + rSum)





print(maxSum)