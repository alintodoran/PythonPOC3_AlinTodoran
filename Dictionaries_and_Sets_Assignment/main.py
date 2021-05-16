from pprint import pprint

import eurostat_data_sets


def group_data_by_year(data_set, needed_year):
    # using provided data_set and year a dictionary is created and returned
    data_by_year = {
        country: [sex, health_index]
        for country, year, sex, health_index in data_set if year == needed_year
    }
    return data_by_year


def group_data_for_germany(data_set):
    # using provided data_set a dictionary for Germany is created and returned
    data_for_germany = {
        year: [sex, health_index]
        for country, year, sex, health_index in data_set if country == 'Germany'
    }
    return data_for_germany


def group_data_by_country_and_year(data_set):
    # using provided data_set a dictionary with key 'Country_year' is created and returned
    data_by_country_and_year = {
        country + '_' + str(year): [sex, health_index]
        for country, year, sex, health_index in data_set
    }
    return data_by_country_and_year


def print_data_by_health_index(data_by_country_and_year, health_index):
    # using provided data_by_country_and_year data for health index > health_index is printed
    for city, data in data_by_country_and_year.items():
        if data[1] > health_index:
            print(city, data)


def print_data_by_health_index_and_sex(data_by_country_and_year, health_index, sex_input):
    # using provided data_by_country_and_year data for health index > health_index and sex == sex_input is printed
    for city, data in data_by_country_and_year.items():
        if data[1] > health_index:
            if data[0] == sex_input:
                print(city, data)


def sets_practice():
    # practicing on 2 sets with 10 items each
    set_a = {1, 5, 7, 3, 97, 43, 99, 12, 2, 55}
    set_b = {7, 52, 77, 3, 15, 78, 9, 66, 12, 99}
    print(f'Original set_a: {set_a}\twith a size of {len(set_a)} elements')
    print(f'Original set_a: {set_b}\twith a size of {len(set_b)} elements\n')

    set_after_union = set_a.union(set_b)
    print(f'Set after union: {set_after_union}\twith a size of {len(set_after_union)} elements\n')

    set_after_intersection = set_a.intersection(set_b)
    print(f'Set after intersection: {set_after_intersection}\twith a size of {len(set_after_intersection)} elements\n')

    set_after_difference_a_to_b = set_a.difference(set_b)
    print(f'Set after difference a to b: {set_after_difference_a_to_b}\twith a size of {len(set_after_difference_a_to_b)} elements')
    set_after_difference_b_to_a = set_b.difference(set_a)
    print(f'Set after difference b to a: {set_after_difference_b_to_a}\twith a size of {len(set_after_difference_b_to_a)} elements\n')

    set_after_symmetric_difference = set_a.symmetric_difference(set_b)
    print(f'Set after symmetric difference: {set_after_symmetric_difference}\twith a size of {len(set_after_symmetric_difference)} elements')


if __name__ == '__main__':
    # get data from "database"
    data_set = eurostat_data_sets.get_data_set()

    print(
        '<---------------------------------------------------------------------------------------------------------->\n'
        '- two dicts that group all data by country for each year\n'
        '> health_index_2017 = {‘France’: [sex, health_index]} > health_index_2017 = {‘France’: [sex, health_index]}\n'
        '<---------------------------------------------------------------------------------------------------------->'
    )
    data_2017 = group_data_by_year(data_set, 2017)
    pprint(data_2017)
    data_2018 = group_data_by_year(data_set, 2018)
    pprint(data_2018)

    print(
        '<---------------------------------------------------------------------------------------------------------->\n'
        '- one dict that groups all data by year for Germany > germany = {2017: [sex, health_index]} \n'
        '<---------------------------------------------------------------------------------------------------------->'
    )
    data_for_germany = group_data_for_germany(data_set)
    pprint(data_for_germany)

    print(
        '<---------------------------------------------------------------------------------------------------------->\n'
        '- one dict that groups all data by country and year, by using year in the key together with the country name\n'
        '> health_index = {‘France_2017’: [year, sex, health_index]}\n'
        '<---------------------------------------------------------------------------------------------------------->'
    )
    data_by_country_and_year = group_data_by_country_and_year(data_set)
    pprint(data_by_country_and_year)

    print(
        '<---------------------------------------------------------------------------------------------------------->\n'
        '- starting from the previous health_index dict, display only the data where the health_index > 5 \n'
        '<---------------------------------------------------------------------------------------------------------->'
    )
    health_index = 5
    print_data_by_health_index(data_by_country_and_year, health_index)

    print(
        '<---------------------------------------------------------------------------------------------------------->\n'
        'starting from the previous health_index dict,display only the data where the health_index > 5 and sex is ‘F’\n'
        '<---------------------------------------------------------------------------------------------------------->'
    )
    health_index = 5
    sex = 'F'
    print_data_by_health_index_and_sex(data_by_country_and_year, health_index, sex)

    print(
        '<---------------------------------------------------------------------------------------------------------->\n'
        'Create two sets with 10 numbers each (some of the numbers should be present in both sets).\n'
        'With these two sets, exemplify the following basic sets operations: union, intersection, difference '
        'and symmetric difference.\n'
        '<---------------------------------------------------------------------------------------------------------->'
    )
    sets_practice()



