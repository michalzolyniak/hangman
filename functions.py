import re
import sys


def load_data(pth: str) -> list:
    """
    :param pth: data path
    :return: data as list
    """
    with open(pth, encoding="utf8") as f:
        data = f.readlines()
    return data


def find_occurrences(word: str, symbol: str, operation: str) -> list:
    """
    :param word:the word where letter or symbol is look for
    :param symbol: letter or expression to find in word
    :param operation: type of operation find one letter or expression in word
    :return: list of indexes in word where letter or expression is occurred
    """
    occurrences = []
    if operation == "letter":
        occurrences = [i for i, letter in enumerate(word) if letter == symbol]
    elif operation == "expression":
        for match in re.finditer(symbol, word):
            occurrences.append([match.start(), match.end()])
    return occurrences


def check_args_parameter(parameter_name) -> bool:
    """
    :param parameter_name: parameter name to find
    :return: True when parameter_name exists in args
    """
    if parameter_name in sys.argv:
        return True
    else:
        return False


def only_polish_letters(tested_string: str) -> bool:
    """
    :param tested_string:
    :return: True when tested_string contains only letters from polish alphabet
    """
    match = re.match("^[aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż]*$", tested_string)
    return match is not None
