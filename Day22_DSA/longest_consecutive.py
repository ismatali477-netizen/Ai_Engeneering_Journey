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
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
