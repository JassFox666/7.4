def common_elements():
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}

    # Перетин множин
    common_set = multiples_of_3 & multiples_of_5
    return common_set


# Перевірка
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')