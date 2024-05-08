def sort_list(lst: list, revers_value):
    lst1 = [float(i.replace("$", '')) for i in lst]
    return sorted(lst1, reverse=revers_value)


def replace_value(lst: list, value):
    lst1 = [float(i.replace(value, '')) for i in lst]
    return lst1

# тест с лямбдой
def sort_list_1(lst: list, revers_value):
    return sorted(lst, key=lambda i: float(i.replace("$", '')), reverse=revers_value)


