def department_initials(l):
    return [x['dept'][0] for x in l]

print(department_initials([
    {"dept":"Artificial Intelligence"},
    {"dept":"Web Development"}
]))
