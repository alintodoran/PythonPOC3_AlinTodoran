import random


def print_main_menu():
    # Main menu for selecting available operations.
    print('\n\t\tChose the wanted operation from the list, only numeric values are allowed:')
    print('1. Show all the items')
    print('2. Sell the latest added item')
    print('3. Sell any item')
    print('4. Add new item')
    print('5. Exit shop')


def get_articles_pool():
    # pool of possible available articles
    articles = ('shirt', 'scarf', 'glove', 'heat', 'jeans', 'skirt', 'dress')
    return articles


def get_sizes_pool():
    # pool of possible available sizes
    sizes = ('XS', 'S', 'M', 'L', 'XL', 'XXL')
    return sizes


def populate_shop(number_of_items):
    # generate randomly two list starting from a predefined pool of elements and a number of items
    random_articles = random.choices(get_articles_pool(), k=number_of_items)
    random_sizes = random.choices(get_sizes_pool(), k=number_of_items)

    # pair each randomly generated article with a randomly generated size
    for x in range(number_of_items):
        shop_items.append((random_articles[x], random_sizes[x]))

    return shop_items


def get_and_validate_input_from_user():
    # get pool values for permitted articles and sizes
    articles_pool = get_articles_pool()
    sizes_pool = get_sizes_pool()
    # a simple while loop that will ask the user for a console input and then compare it to a pool of values
    # as long as the input is not valid (not found in the pool) the user will be spammed
    exit_condition = True
    while exit_condition:
        print(f'Chose one of the following: {articles_pool}')
        article = input()
        if article in articles_pool:
            exit_condition = False
        else:
            print('Input not valid, please retry!')
    # a simple while loop that will ask the user for a console input and then compare it to a pool of values
    # as long as the input is not valid (not found in the pool)  the user will be spammed
    exit_condition = True
    while exit_condition:
        print(f'Chose one of the following: {sizes_pool}')
        size = input()
        if size in sizes_pool:
            exit_condition = False
        else:
            print('Input not valid, please retry!')
    # return the validated user input
    return article, size


def sell_latest_item(shop_items):
    # function to remove the latest added item
    # procedure done only if there are items in the list
    if len(shop_items) > 0:
        print('Latest item sold!')
        shop_items.pop()
    else:
        print('Shop is empty, new products are coming soon!')
    return shop_items


def sell_specific_item(shop_items):
    # function to remove any desired item
    # procedure done only if there are items in the list
    if len(shop_items) > 0:
        validated_element_from_user = get_and_validate_input_from_user()
        if validated_element_from_user in shop_items:
            print(f'Item {validated_element_from_user} sold!')
            shop_items.remove(validated_element_from_user)
        else:
            print('Item not found in the shop, please chose something else!')
    else:
        print('Shop is empty, new products are coming soon!')
    return shop_items


def add_item(shop_items):
    # ask for user input, validate it and then add it to the list
    validated_element_from_user = get_and_validate_input_from_user()
    shop_items.append(validated_element_from_user)
    return shop_items


if __name__ == '__main__':
    # populate the shop with a certain amount of randomly generated items
    # number_of_items can be set to any wanted value, 9 was used to not fill all the console when menu option 1 is used
    number_of_items = 2
    shop_items = []
    shop_items = populate_shop(number_of_items)

    # a simple user friendly console menu
    exit_condition = True
    while(exit_condition):
        print_main_menu()
        input_from_user = input()
        if input_from_user == '1':
            print(shop_items)
        elif input_from_user == '2':
            shop_items = sell_latest_item(shop_items)
        elif input_from_user == '3':
            shop_items = sell_specific_item(shop_items)
        elif input_from_user == '4':
            shop_items = add_item(shop_items)
        elif input_from_user == '5':
            exit_condition = False
            print('See you later!')
        else:
            print('Input not valid, please retry!')


