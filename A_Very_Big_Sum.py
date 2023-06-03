def aVeryBigSum(ar, n):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the array and accumulate the sum
    for i in range(n):
        sum += ar[i]
    return sum
        # Read the size of the array
n = int(input())
# Read the array elements
ar = list(map(int, input().split()))
# Call the function and print the sum of the elements
result = aVeryBigSum(ar, n)
print(result)