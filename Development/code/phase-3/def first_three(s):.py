def first_three(s):
    if len(s) < 3:
        return s
    else:
        return s[:3]

print(first_three('ipy'))
print(first_three('python'))
