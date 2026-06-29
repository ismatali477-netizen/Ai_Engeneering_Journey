def longest_consecutive(l):
    count=1
    max_streak=0
    s=sorted(set(l))
    for i in range(len(s)-1):
        nxt=s[i]+1
        if s[i+1]==nxt:
            count+=1
        else:
            max_streak = max(max_streak, count)
            count= 1
    max_streak = max(max_streak, count)
    return max_streak   
print(longest_consecutive([1,2,10,11,12]))
