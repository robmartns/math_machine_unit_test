import pytest

def math_machine (n1, operator, n2):
    if type(n1) != int or type(n2) != int:
        raise Exception('Only ints are accepted!')