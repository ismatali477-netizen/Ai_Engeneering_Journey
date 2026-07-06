def group_anagrams(l):
    ans={}
    for item in l:
        key="".join(sorted(item))
        if key not in ans:
            ans[key]=[]
        ans[key].append(item)
    return list(ans.values())
print(group_anagrams(
    ["eat","tea","tan","ate","nat","bat"]
))
