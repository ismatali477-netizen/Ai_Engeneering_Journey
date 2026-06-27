def group_by_length(l):
    d = {}

    for item in l:
        length = len(item)

        if length not in d:
            d[length] = []

        d[length].append(item)

    return d

print(group_by_length(["hi", "cat", "dog", "hello"]))
