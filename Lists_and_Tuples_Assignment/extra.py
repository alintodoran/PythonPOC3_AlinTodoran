def remove_element_from_tuple():
    # Write a python code to remove an element from a tuple
    tuple_exemple = (1, 2, 3, 4)
    print(f'Original:{tuple_exemple} of type {type(tuple_exemple)}')
    tuple_exemple = list(tuple_exemple)
    tuple_exemple.append(5)
    tuple_exemple = tuple(tuple_exemple)
    print(f'After modification:{tuple_exemple} of type {type(tuple_exemple)}')


def replace_the_last_element():
    # Replace the last element in the list with the string 'last' using list comprehension and tuples
    list_example = ['a', 'b', 'c', 'd']
    # ...loading...no idea
    print(list_example)


def extract_strings():
    # Extract only the strings from the following list using list comprehension
    slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
    print(slist)
    slist_extracted = [slist[x] for x in range(len(slist)) if isinstance(slist[x], str)]
    print(slist_extracted)


def generate_matrix():
    #Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest
    matrix = []
    line_list = []
    for x in range(3):
        for y in range(3):
            if x == y:
                line_list.append('X')
            else:
                line_list.append('_')
        matrix.append(line_list)
        line_list = []
    print(matrix)


if __name__ == '__main__':
    remove_element_from_tuple()
    print('---------------------------------------\n')
    replace_the_last_element()
    print('---------------------------------------\n')
    extract_strings()
    print('---------------------------------------\n')
    generate_matrix()
