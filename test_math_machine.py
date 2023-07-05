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
    test_non_int_input_for_n1
    test_non_int_input_for_n2
    test_addition_with_negative_result
    test_addition_with_small_result
    test_addition_with_medium_result
    test_addition_with_large_result
    test_multiplication_with_negative_result
    test_multiplication_with_small_result
    test_multiplication_with_medium_result
    test_multiplication_with_large_result
    test_invalid_operator