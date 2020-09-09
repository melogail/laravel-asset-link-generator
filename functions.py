#! python3

import sys

def check_sys_arg(index, error_message, input_message):
    """ Check if system arguments are added or not

    :param index:               System argument number
    :param error_message:       Error message to be displayed
    :param input_message:       Input message to be displayed
    :return:
    """
    arg = False
    try:
        arg = sys.argv[index]
        return arg

    except IndexError:
        print(error_message)
        while not arg:
            arg = input(input_message + ': ')
        return arg
