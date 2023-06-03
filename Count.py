def count_even_odd_registration_codes(N, codes):
    even_count = 0
    odd_count = 0
    for code in codes:
        if int(code) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f"{even_count} {odd_count}"
N = int(input())
codes = input().split()
result = count_even_odd_registration_codes(N, codes)
print(result)