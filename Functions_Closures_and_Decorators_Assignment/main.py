from pprint import pprint
import eurostat_database
import decorators


def prepare_data(description, raw_data):
    # function that prepares the dataset
    prepared_data = {}
    # get the list of the years (columns)
    year_data = description[1]

    for country, data in raw_data:
        # iterate through each element of raw_data list
        temp_list = []
        for year in range(len(year_data)):
            # for each year, extract raw data and store it as a list of dictionaries
            temp_dictionary = {year_data[year]: (data[year])}
            temp_list.append(temp_dictionary)
        # populate an auxiliary dictionary that will be added to our final dictionary
        prepared_data_aux = {country: temp_list}
        prepared_data.update(prepared_data_aux)

    return prepared_data


def return_data_by_year(data, year):
    # retrieve data for desired year
    data_by_year = []
    # get key and value for each dictionary element
    for country, values in data.items():
        # get list data (list of dictionaries for each year)
        for list_data in values:
            # if valid data is found for needed year, create a dictionary and add it to our return value
            if list_data.get(year):
                temp_dictionary = {country: list_data.get(year)}
                data_by_year.append(temp_dictionary)
    return data_by_year


def return_data_by_country(data, country):
    # retrieve data for desired country
    # we have a dictionary as an input (data), get method can be used to access a desired jey (country in this case)
    data_by_country = data.get(country)
    return data_by_country


def return_average_by_country(data):
    # perform average from an iterable
    sum_of_elements = 0
    number_of_elements = 0
    # we go through each element of the list (n dictionaries), get the value and convert it to a list
    for items in data:
        test = list(items.values())
        # check if the list item extracted above is numeric(we know we work with % so we will have only positive values)
        if test[0].isdigit():
            sum_of_elements += int(test[0])
            number_of_elements += 1
    # return the basic formula for a simple average
    return sum_of_elements / number_of_elements


if __name__ == '__main__':
    # get data from database
    description = eurostat_database.get_description_data()
    raw_data = eurostat_database.get_raw_data()

    # prepare the dataset
    print('------------------- prepare the dataset ----------------')
    prepared_data = prepare_data(description, raw_data)
    pprint(prepared_data)

    # retrieve data for each year
    print('------------------- retrieve data for desired year ----------------')
    year = '2018'
    data_by_year = return_data_by_year(prepared_data, year)
    pprint(data_by_year)

    # retrieve data for each country
    print('------------------- retrieve data for desired country ----------------')
    country = 'XK'
    data_by_country = return_data_by_country(prepared_data, country)
    pprint(data_by_country)

    # perform average from an iterable(of year data or country data)
    print('------------------- perform average from an iterable ----------------')
    average_by_country = return_average_by_country(data_by_country)
    pprint(average_by_country)

    # decorators assignment
    print('------------------- decorators ----------------')
    decorators.main_decorators_call()

