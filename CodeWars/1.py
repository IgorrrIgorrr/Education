def solve(arr):
    a =[]
    b = sorted(arr)
    while b != []:
        q = b.pop(-1)
        a.append(q)
        if b != []:
            q = b.pop(0)
            a.append(q)
    return(a)

print(solve([15,11,10,7,12]))