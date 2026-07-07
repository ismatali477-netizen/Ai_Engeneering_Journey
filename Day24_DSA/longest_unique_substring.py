def longest_unique_substring(s):
    seen=set()
    count=0
    left=0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        count=max(count,right-left+1)
    return count
print(longest_unique_substring("abba"))