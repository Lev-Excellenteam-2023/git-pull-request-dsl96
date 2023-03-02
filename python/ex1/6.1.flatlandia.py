# week 6 ex3 שטוחלנדיה
import os
def find_special_state(path = None):
    if not path:
        path = os.path.join(os.getcwd(), 'resource', 'states.txt')

    states = open(path, 'r').read().split()

    def check_if_string_in_one_line_keyboard(string):
        string_set = set(string.lower())

        line1 = {'e', 'i', 'o', 'p', 'q', 'r', 't', 'u', 'w', 'y'}
        line2 = {'a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's'}
        line3 = {'b', 'c', 'm', 'n', 'v', 'x', 'z'}

        return string_set <= line1 or string_set <= line2 or string_set <= line3

    return [state for state in states if check_if_string_in_one_line_keyboard(state)]

