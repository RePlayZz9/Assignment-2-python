def all_eq(lst):
    max_len = max(len(s) for s in lst)
    return [s + '_' * (max_len - len(s)) for s in lst]

# Пример использования (тест не обязателен, но может быть полезен)
if __name__ == "__main__":
    strings = input().split()  # например: "a bb ccc"
    result = all_eq(strings)
    print(result)