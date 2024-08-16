def find_unique_value(some_list):
    set_from_some_list = set(some_list)
    unique_values = []
    for value in set_from_some_list:
        if some_list.count(value) == 1:
            unique_values.append(value)

    print(f"Unique values for {some_list}: {unique_values}")

    if len(unique_values) > 1:
        return unique_values
    else:
        return unique_values[0]


find_unique_value([1, 2, 1, 1, 4])
find_unique_value([2, 3, 3, 3, 5, 5])
find_unique_value([5, 5, 5, 2, 2, 0.5])
