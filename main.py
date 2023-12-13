str_list1 = ['Hello', '2', 'world', ':-)']
str_list2 = ['1234', '1567', '-2', 'computer science']
str_list3 = ['Russia', 'Denmark', 'Kazan']


def input_user_list():
    size = int(input('Input size of list for search element: '))
    user_str = list()
    for index in range(size):
        arg = str(input(f'Input {index + 1} member of your list: '))
        user_str.insert(index, arg)
    return user_str


def create_new_list(list_1):
    new_list = list()
    index = 0
    for item in list_1:
        if len(item) <= 3:
            new_list.insert(index, item)
            index += 1
    return new_list


print(create_new_list(str_list1))
print(create_new_list(str_list2))
print(create_new_list(str_list3))
print(create_new_list(input_user_list()))
