def add_one(some_list):

    string_from_some_list = ''

    for i in some_list:
        string_from_some_list += str(i)

    final_number_from_some_list = int(string_from_some_list) + 1

    final_list = []
    for i in str(final_number_from_some_list):
        final_list.append(int(i))

    print(f"Origin list: {some_list} => Final list: {final_list}")


add_one([1, 2, 3, 4])
add_one([9, 9, 9])
add_one([0])
add_one([9])
