height = [1,8,6,2,5,4,8,3,7]
MaxArea = 0

l, r = 0, len(height) - 1

while l < r:
    MaxArea = max(min(height[l], height[r]) * (r - l), MaxArea)
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

print(MaxArea)
