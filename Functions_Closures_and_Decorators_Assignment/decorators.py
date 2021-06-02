def uppercase_decorator(fun):
    # decorator will uppercase the result
    def uppercase_wrapper(what_to_say):
        what_to_say = what_to_say.upper()
        fun(what_to_say)

    return uppercase_wrapper

def register(fun):
    # decorator will update a list called print_registry with all the decorated functions names
    # no idea how to do this point, I am just practicing here
    print_registry = []
    def register_wrapper(*args):
        fun(*args)
        print_registry.append(fun.__name__)
        print(print_registry)
    return register_wrapper

@uppercase_decorator
@uppercase_decorator
@register
def my_string_function(what_to_say):
    print(what_to_say)


def safe_division(fun):
    # decorator will check the second argument of the function before performing the division
    def test_wrapper(first_number, second_number):
        if second_number == 0:
            return None
        else:
            fun(first_number, second_number)
    return test_wrapper


@safe_division
def my_math_division_function(first_number, second_number):
    print(first_number / second_number)


def main_decorators_call():
    # Create a decorator called uppercase that will uppercase the result
    my_string_function('Hello there!')

    # Create a decorator called safe_addition that will output a message if the operation cannot be performed correctly
    # [is unsafe] and return a correct result [check - floating point inaccuracies],
    # otherwise it will return just the result
    first_number = 9
    second_number = 3
    my_math_division_function(first_number, second_number)

    # Create a decorator called register that will update a list called print_registry with all the decorated functions
    # names.
