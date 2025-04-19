def matmul(A, B):
    if len(A[0]) != len(B):
        return f"multiplication not possible for matrices of size {len(A)}x{len(A[0])} and {len(B)}x{len(B[0])}"
    else:
        C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        s = ""
        for i in range(len(C)):
            for j in range(len(C[0])):
                for k in range(len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]
                s += str(C[i][j]) + " "
            s += "\n"
        return s

def main():
    r1, c1 = map(int, input("enter number of rows and columns for matrix 1: ").split())
    m1 = []
    for i in range(r1):
        l = list(map(int, input(f"enter {c1} numbers for the entries of row {i}: ").split()))
        m1.append(l)

    r2, c2 = map(int, input("enter number of rows and columns for matrix 2: ").split())
    m2 = []
    for i in range(r2):
        l = list(map(int, input(f"enter {c2} numbers for the entries of row {i}: ").split()))
        m2.append(l)

    print(matmul(m1, m2))

main()
