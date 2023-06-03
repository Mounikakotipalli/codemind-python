def sum_of_elements(arr):
    sum = 0
    for row in arr:
        for element in row:
            sum += element
    return sum
M = int(input())
N = int(input())
arr = []
for _ in range(M):
    row = list(map(int, input().split()))
    arr.append(row)
    result = sum_of_elements(arr)
print(result)