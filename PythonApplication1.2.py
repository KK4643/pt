def count_matches(s1, s2):

    # Формируем множество биграмм первой строки
    bigrams1 = set()
    for i in range(len(s1) - 1):
        bigrams1.add(s1[i:i+2])

    # Формируем множество биграмм второй строки
    bigrams2 = set()
    for i in range(len(s2) - 1):
        bigrams2.add(s2[i:i+2])

    # Находим пересечение множеств
    return len(bigrams1 & bigrams2)


# Примеры использования:
print(count_matches("xadasw", "xad"))       # 2  ("xa", "ad")
print(count_matches("hello", "hell"))       # 3  ("he", "el", "ll")
print(count_matches("abc", "xyz"))          # 0
print(count_matches("a", "b"))              # 0  (нет биграмм)
print(count_matches("", "abc"))             # 0
