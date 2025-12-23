s = input().strip()
count = 0
n = len(s)
for i in range(n - 4):
    substr = s[i:i+5]
    if substr == '>>-->' or substr == '<--<<':
        count += 1
print(count)