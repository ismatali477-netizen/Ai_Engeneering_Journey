from collections import Counter
def character_replacement(s, k):
    count=0
    answer=0
    left=0
    for right in range(len(s)):
        window=s[left:right+1]
        max_freq=max(Counter(window).values())
        while len(window)-max_freq>k:
            left+=1
            window=s[left:right+1]
            if window:
                max_freq=max(Counter(window).values())
        answer=max(answer,len(window))
    return answer
print(character_replacement("ABAB", 1))
