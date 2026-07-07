def max_sum_subarray(l,k):
    current_sum=[]
    old_sum=sum(l[0:k])
    current_sum.append(old_sum)
    left=0
    for right in range(k,len(l)):
        outgoing=l[left]
        incoming=l[right]
        new_sum = old_sum - outgoing + incoming
        current_sum.append(new_sum)
        old_sum=new_sum
        left+=1
    return max(current_sum)
print(max_sum_subarray([2,1,5,1,3,2], 3))
