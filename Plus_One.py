def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:digits[i] = 0
        # If all digits are 9, we need to add an additional digit
    digits.insert(0, 1)
    return digits
        # Read the length of the array
N = int(input())
# Read the array elements
digits = list(map(int, input().split()))
# Call the function to add one to the integer
result = plusOne(digits)
# Print the updated array
print(*result)