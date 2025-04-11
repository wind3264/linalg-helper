def two(m):
    # m is a 2x2 matrix
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def cofactor(m):
    # find the determinant by reducing to 2x2s
    k = 0
    if len(m) > 2 :
        j = 1
        for i in range(len(m)) :
            k += m[0][i] * j * cofactor([x[:i] + x[i+1:] for x in m[1:]])
            j *= -1
    else :
        k = two(m)
    return k

def main():
    # driver code
    det = 0
    n = int(input("enter number of rows: "))
    arr = []
    for i in range(n) :
        l = list(map(int, input(f"enter the entries of row {i}, separated by spaces: ").split()))
        arr.append(l)
    if n == 1:
        det = arr[0][0]
    elif n == 2:
        det = two(arr)
    else:
        det = cofactor(arr)
    print(f"the determinant of your matrix is {det}.")

main()
