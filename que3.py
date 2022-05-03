def rotation_check(s1, s2):
    if len(s1) == len(s2):
        temp = s1 + s1
        if temp.count(s2) > 0:
            return 1
    else:
        return 0
s1 = "ABCD"
s2 = "BCDA"
if rotation_check(s1, s2):
    print("Strings are rotation of each other")
else:
    print("Strings are not rotation!")