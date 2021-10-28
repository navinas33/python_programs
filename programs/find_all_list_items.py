def find_all_index(items, value):
    final_list = list()
    for index, item in enumerate(items):
        if item == value:
            final_list.append([index])
        elif isinstance(item, list):
            for i in find_all_index(item, value):
                final_list.append([index] + i)
    return final_list


def main():
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    # example = [[1, 2, 3]]
    print(find_all_index(example, 2))


if __name__ == '__main__':
    main()
