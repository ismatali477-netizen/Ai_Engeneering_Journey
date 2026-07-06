def two_sum_sorted(l,m):
    left=0
    right=len(l)-1
    while left<right:
        sum=l[left]+l[right]
        if sum==m:
            return [left,right]
        elif sum<m:
            left+=1
        else:
            right-=1
print(two_sum_sorted([2,7,11,15], 9))
