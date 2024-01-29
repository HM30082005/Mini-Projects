# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [0, 4, 1, 2, 3, 4]
height = [4,2,0,3,2,5]

def findbig(n):
    l, r = n, n
    while height[n] >= height[l]:
        l -= 1
        if l == -1:
            break

    while height[n] >= height[r]:
        r += 1
        if r == len(height):
            break

    return l, r
            
def water_area(l, r):
    water = 0
    # print("\n\n––––––––––––––––––––––––––––––––––––––––––––––\n")
    # print("Water Area Logs")
    h = min(height[l], height[r])
    # print(f"h is {h}")
    for i in range (l + 1, r):
        water += max(h - height[i], 0)
        # print(f"when i is {i} \t height[i] is {height[i]} \t new height[i] is {h} \t ∂ water is {max(h - height[i], 0)}")
        height[i] = h
    # print("\n––––––––––––––––––––––––––––––––––––––––––––––\n\n")
    return water


i = 1
l, r = 0, 0
res = 0
while i > 0 and i < len(height):
    l, r = findbig(i)
    # print(f"when i is {i} \t l is {l} \t r is {r}")
    if l == -1 or r == len(height):
        i += 1
        continue
    res += water_area(l, r)
    # print(f"\t  \t when i is {i} \t water is {water_area(l, r)}")
    i = r 

print(res)
print(height)