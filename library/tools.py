import sys


def print_obj(obj, mode: str = 'a', destination: str = '') -> None:
    """
    Write the records on consolle or on the chosen destination

    :param obj: string or list or printable object
    :param mode: is 'w', 'a', ...
    :param destination: if empty is consolle else indicates the destination (file, ...)
    :return: None
    """
    if len(destination) > 0:
        # crea o svuota il file
        file_out = open(destination, mode)
        print(obj, file=file_out)
        file_out.close()
    else:
        print(obj)


def string_to_list(string: str, separator: str) -> list:
    """
    From list to string

    :param string:
    :param separator:
    :return: list of values from the string
    """
    result = string.split(separator)

    return result


def replace_string_element(original_string: str, substitution_list: list) -> str:
    """
    Replace a list of items into the original string

    :param original_string: string
    :param substitution_list: Each element is ('actual value', 'new value')
    :return: updated string
    """
    result = original_string

    for element in substitution_list:
        result = result.replace(element[0], element[1])

    return result


def replace_list_elements(original_elements: list, new_elements: list) -> list:
    """
    Replace a list of elements into original list

    :param original_elements:
    :param new_elements: each element is ('actual value', 'new value')
    :return:
    """
    result = []

    for value in original_elements:
        for element in new_elements:
            if value == element[0]:
                result.append(element[1])

    return result


def find_in_list(string: str, my_list: list) -> int:
    """
    Find a string into a list

    :param string:
    :param my_list:
    :return: 0 = success
    """
    result = 0

    if not (string in my_list):
        result = 1

    return result


def remove_bad_chars(string_from_csv: str) -> list:
    result = []
    string_from_csv = string_from_csv.replace("'", "")
    string_from_csv = string_from_csv.replace(" ", "")

    temporary_list = string_from_csv.splitlines()
    for element in temporary_list:
        result.append(element.split(','))

    return result


def platform_wrapper(path):
    """
    Manage the path

    :param path:
    :return: the path format for the current platform
    """
    result = path

    if 'win' in sys.platform:
        result = path.replace('/', '\\')

    return result
