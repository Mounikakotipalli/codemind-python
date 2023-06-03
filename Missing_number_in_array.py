def find_missing_number(arr, N):
    # Calculate the sum of the first N natural numbers
    sum_N = (N * (N + 1)) // 2
    # Calculate the sum of the array elements
    sum_arr = sum(arr)
    # The missing number is the difference between the sum of N and the sum of array elements
    missing_number = sum_N - sum_arr
    return missing_number
# Read the number of test cases
T = int(input())
for _ in range(T):
    # Read the size of the array
    N = int(input())
    # Read the array elements
    arr = list(map(int, input().split()))
    # Call the function and print the missing number
    missing_number = find_missing_number(arr, N)
    print(missing_number)