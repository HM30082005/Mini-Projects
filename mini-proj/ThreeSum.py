nums = [-1,0,1,2,-1,-4]
nums = sorted(nums)
ans = []
# print("wassup")
# print(range(len(nums) - 2))
for i in range(0, len(nums) - 2):
    # print("Hello")
    if i > 0:
        # print(f"hi {i} and {nums[i]} and {nums[i-1]}")
        if nums[i] == nums[i - 1]:
            # print(f"fi {i}")
            continue
    if nums[i] > 0:
        break
    l, r = i + 1, len(nums) - 1
    while l < r:
        sum = nums[i] + nums[l] + nums[r]
        # print(sum)
        if sum == 0:
            # print(f"dam {i}")
            ans.append([nums[i], nums[l], nums[r]])
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            l += 1
            r -= 1
        if sum < 0:
            l += 1
        if sum > 0:
            r -= 1
print(ans)
    
            
