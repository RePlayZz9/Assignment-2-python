a = input().strip()
b = input().strip()

def get_cyclic_shifts(s):
    shifts = set()
    n = len(s)
    for k in range(n):
        shifts.add(s[k:] + s[:k])
    return shifts

shifts_b = get_cyclic_shifts(b)
count = 0
n, m = len(a), len(b)

for i in range(n - m + 1):
    substr = a[i:i+m]
    if substr in shifts_b:
        count += 1

print(count)