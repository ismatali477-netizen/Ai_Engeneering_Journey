def average_passed_marks(l):
    passed = [x["marks"] for x in l if x["marks"] >= 40]
    return sum(passed) / len(passed)
print(average_passed_marks([
    {"name":"Ali","marks":80},
    {"name":"Sara","marks":30},
    {"name":"John","marks":50}
]))
