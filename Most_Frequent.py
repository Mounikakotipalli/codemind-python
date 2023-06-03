from collections import Counter
N = int(input())
numbers = list(map(int, input().split()))
frequency = Counter(numbers)
max_frequency = max(frequency.values())
most_frequent_number = min([num for num, freq in frequency.items() if freq == max_frequency])
print(most_frequent_number)