n, m = map(int, input().split())
s = input().strip()

substrings = set()
for i in range(n - m + 1):
    substr = s[i:i+m]
    substrings.add(substr)

print(len(substrings))