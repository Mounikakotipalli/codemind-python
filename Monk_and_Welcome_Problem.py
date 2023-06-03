N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for i in range(N):
    C.append(A[i] + B[i])
for num in C:
    print(num, end=' ')