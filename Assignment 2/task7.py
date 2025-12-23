from collections import Counter

items = input().split()

cnt = Counter(items)

# 1. Частоты
print("Purchase frequency:")
for item, freq in cnt.items():
    print(f"{item}: {freq}")

# 2. Самый популярный
most_common = cnt.most_common(1)[0][0]
print("Most popular item:", most_common)

# 3. Куплено ровно 1 раз
once = [item for item, freq in cnt.items() if freq == 1]
print("Purchased once:", " ".join(once))

# 4. Сортировка по убыванию частоты
sorted_items = cnt.most_common()
print("Sorted by frequency:")
for item, freq in sorted_items:
    print(item, freq)