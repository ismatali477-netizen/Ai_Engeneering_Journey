def smallest_subarray(m,l):
    left = 0
    window_sum = 0
    min_length = float('inf')
    for right in range(len(l)):
        window_sum += l[right]
        while window_sum >= m:
            min_length=min(min_length,right-left+1)
            window_sum -= l[left]
            left += 1    
    return min_length       
print(smallest_subarray(7, [2,1,5,2,3,2]))