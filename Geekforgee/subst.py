def isSubset( a1, a2, n, m):
    for i in a2:
        if a1.count(i) < a2.count(i):
            return "No"
    return "Yes"
