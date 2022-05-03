def myfunc(n, A, C, B):
    if n == 0:
        return
    myfunc(n-1, A, B, C)
    print("Move disk", n, "from rod", A, "to rod", C)
    myfunc(n-1, B, C, A)

n = int(input())
myfunc(n, 'A', 'C', 'B')