def max_area(heights):
    left = 0
    right = len(heights) - 1
    max_water=0
    while left < right:
        area = (right - left) * min(heights[left], heights[right])

        max_water=max(max_water,area)
        if heights[left]<heights[right]:
            left+=1
        else:
            right-=1
    return max_water
print(max_area([1,8,6,2,5,4,8,3,7]))
