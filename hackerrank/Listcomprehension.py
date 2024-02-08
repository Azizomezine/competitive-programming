def permus3d_comprehension(x, y, z, n):
    x = range(int(x) + 1)
    y = range(int(y) + 1)
    z = range(int(z) + 1)

    return [[i,j,k] for i in x for j in y for k in z if i+j+k!=n]
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(permus3d_comprehension(x, y, z, n))
        
        
        
