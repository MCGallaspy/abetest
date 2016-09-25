
def problem_1(a, b):
    """ Write a function of two arguments that returns `True` if adding both of its
        arguments would result in an `int`. Otherwise `false`.
    """
    return type(a + b) == int
    
def problem_2(number_str_1, number_str_2):
    """ Given two strings, return `True` if adding both those numbers in Python
        would result in an `int`. Otherwise if it would return something else, like
        a `float`, return `False`.
        
        For example if you got "4" and "3.5", you would return `False`.
        
        Assume that the strings passed in only contain valid numbers with no whitespace,
        for example won't get "foobar", "  5.56  ", or "3.3.3".
    """
    one_is_int, two_is_int = "." not in number_str_1, "." not in number_str_2
    return one_is_int and two_is_int

def problem_3(x):
    y = 0
    # Because we equipped our mock class with a total ordering behind the scenes,
    # even odd implementations like this will pass the test.
    while True:
        x -= 1
        # This works too
        # x = x - 1
        y += 1
        if x == 0:
            break
    return x, y