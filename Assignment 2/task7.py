from collections import Counter

items = input().split()

cnt = Counter(items)

print("Purchase frequency:")
for item, freq in cnt.items():
    print(f"{item}: {freq}")

most_common = cnt.most_common(1)[0][0]
print("Most popular item:", most_common)

once = [item for item, freq in cnt.items() if freq == 1]
print("Purchased once:", " ".join(once))

sorted_items = cnt.most_common()
print("Sorted by frequency:")
for item, freq in sorted_items:
    print(item, freq)