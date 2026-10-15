def sum_without_13(nums):
   
    total = 0
    for num in nums:
        if num == 13:
            break
        total += num
    return total


# Примеры использования:
print(sum_without_13([1, 2, 3, 13, 4]))          # 6
print(sum_without_13([1, 2, 3, 4, 5]))           # 15
print(sum_without_13([13, 1, 2, 3]))             # 0
print(sum_without_13([1, 13, 2, 13, 3]))         # 1
print(sum_without_13([]))                        # 0
