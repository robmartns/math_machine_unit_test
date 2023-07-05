import pytest

def math_machine (n1, operator, n2):
    if type(n1) != int or type(n2) != int:
        raise Exception('Only ints are accepted!')
    
    if operator == '+':
        Result = n1 + n2
    elif operator == '*':
        Result = n1 * n2
    else:
        raise Exception(f"Math Machine doesn't recognize '{operator}'")
    
    if Result < 0:
        return 'A negative number. What does that mean?'
    elif Result < 10:
        return 'A small number. I can deal with that!'
    elif Result < 20:
        return 'A medium-sized number. OK'
    else:
        return 'Way too big for me to handle!'
    
class Test_MathMachine:
    def test_non_int_input_for_n1(self):

    def test_non_int_input_for_n2(self):

    def test_addition_with_negative_result(self):
        assert 'A negative number. What does that mean?' in math_machine(-2, '+', -2)

    def test_addition_with_small_result(self):
        assert 'A small number. I can deal with that!' in math_machine(2, '+', 2)

    def test_addition_with_medium_result(self):
        assert 'A medium-sized number. OK' in math_machine(9, '+', 9)

    def test_addition_with_large_result(self):
        assert 'Way too big for me to handle!' in math_machine(14, '+', 14)

    def test_multiplication_with_negative_result(self):
        assert 'A negative number. What does that mean?' in math_machine(2, '*', -2)

    def test_multiplication_with_small_result(self):
        assert 'A small number. I can deal with that!' in math_machine(2, '*', 2)

    def test_multiplication_with_medium_result(self):
        assert 'A medium-sized number. OK' in math_machine(3, '*', 5)

    def test_multiplication_with_large_result(self):
        assert 'Way too big for me to handle!' in math_machine(5, '*', 5)

    def test_invalid_operator(self):