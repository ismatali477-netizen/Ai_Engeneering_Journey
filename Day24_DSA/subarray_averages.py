def subarray_averages(l,k):
    current_avg=[]
    old_sum=sum(l[0:k])
    current_avg.append(old_sum/k)
    left=0
    for right in range(k,len(l)):
        outgoing=l[left]
        incoming=l[right]
        new_sum=old_sum - outgoing + incoming
        new_avg = new_sum/k
        current_avg.append(new_avg)
        old_sum=new_sum
        left+=1
    return current_avg
print(subarray_averages([1,3,2,6,-1,4,1,8,2], 5))
