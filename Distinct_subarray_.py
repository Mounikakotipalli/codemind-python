def count_odd_sum_subarrays(L, R):
    prefix_sums = [0]
    for i in range(L, R + 1):
        prefix_sums.append(prefix_sums[-1] + i)
    count = 0
    for i in range(len(prefix_sums)):
        for j in range(i + 1, len(prefix_sums)):
            if (prefix_sums[j] - prefix_sums[i]) % 2 == 1:
                count += 1
    return count
L = int(input())
R = int(input())
result = count_odd_sum_subarrays(L, R)
print(result)