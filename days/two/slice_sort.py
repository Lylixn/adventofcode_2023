from days.two.sort import Sort


def slice_sort(string: str):
    sort_list: list[Sort] = []
    sorts = string.split(';')

    for sort in sorts:
        sort_list.append(Sort(sort))

    return sort_list
