def reverse_dict(d):
    return {d[item]:item for item in d}
print(reverse_dict({
    "Ali": 80,
    "Sara": 90
}))
