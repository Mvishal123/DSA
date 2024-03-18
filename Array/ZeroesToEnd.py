def pushZeroEnd(nums):
    if len(nums) <= 1:
        print(nums)
    else:
        i = 0
        j = 1

        while i < len(nums) and j < len(nums):
            while nums[i] != 0 and i < len(nums):
                i += 1
                # j += 1

            while nums[j] == 0 and j < len(nums):
                j += 1

            if i >= len(nums):
                break
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
                i += 1

    print(nums)


ls = [2, 1]
pushZeroEnd(ls)
