def non_repeated(str1):
    for i in str1:
        count = str1.count(i)
        if count == 1:
            return i
            break
str1 = "vaibhav"
non_repeated(str1) 