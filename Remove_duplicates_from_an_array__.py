N = int(input())
array = list(map(int, input().split()))
unique_set = set(array)
unique_list = list(unique_set)
print(*unique_list)