def weightMachine(N, weights, T):
    base_amount = 1 
    # Base amount to be paid
    total_amount = 0 
    # Total amount to be paid
    # Iterate through the array of weights
    for weight in weights:
        if weight > T:
            total_amount += 2 * base_amount 
    # Double the base amount
        else:
            total_amount += base_amount
    return total_amount
    # Read the number of luggage
N = int(input())
# Read the weights of each luggage
weights = []
for _ in range(N):
    weight = int(input())
    weights.append(weight)
    # Read the weight threshold
T = int(input())
# Call the function to calculate the required amount to be paid
amount = weightMachine(N, weights, T)
# Print the required amount to be paid
print(amount)