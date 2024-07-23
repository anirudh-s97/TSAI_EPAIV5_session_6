import session6

from session6 import find_docstring
from session6 import fibonacci_closure
from session6 import function_call_counter
from session6 import flexible_function_call_counter


def test_check_docstring():
    @find_docstring(50)
    def func_with_long_docstring():
        """This is a long docstring that is definitely more than 50 characters long."""
        pass
    
    @find_docstring(50)
    def func_with_short_docstring():
        """short docstring."""
        pass
    
    @find_docstring(50)
    def func_without_docstring():
        ""
        pass
    
    @find_docstring(50)
    def func_with_exactly_50_chars():
        """This docstring is exactly fifty characters long...."""
        pass
    
    assert func_with_long_docstring() == True
    assert func_with_short_docstring() == False
    assert func_without_docstring() == False
    assert func_with_exactly_50_chars() == False

def test_fibonacci_closure():
    fib = fibonacci_closure()
    assert fib() == 1
    assert fib() == 1
    assert fib() == 2
    assert fib() == 3
    assert fib() == 5

def test_function_call_counter():
    global_dict = {}
    counter = function_call_counter(global_dict)
    
    counter['add'](2, 3)
    counter['mul'](4, 5)
    counter['div'](10, 2)
    counter['add'](1, 1)
    
    assert global_dict == {'add': 2, 'mul': 1, 'div': 1}
    
    counter['mul'](2, 2)
    counter['div'](8, 4)
    
    assert global_dict == {'add': 2, 'mul': 2, 'div': 2}

def test_flexible_function_call_counter():
    create_counter = flexible_function_call_counter()
    
    dict1 = {}
    counter1 = create_counter(dict1)
    counter1['add'](2, 3)
    counter1['mul'](4, 5)
    
    dict2 = {}
    counter2 = create_counter(dict2)
    counter2['div'](10, 2)
    counter2['add'](1, 1)
    
    assert dict1 == {'add': 1, 'mul': 1}
    assert dict2 == {'div': 1, 'add': 1}
    
    counter1['add'](5, 5)
    counter2['mul'](3, 3)
    
    assert dict1 == {'add': 2, 'mul': 1}
    assert dict2 == {'div': 1, 'add': 1, 'mul': 1}

# Additional test cases to check boundary conditions

def test_check_docstring_edge_cases():
    @find_docstring(0)
    def func_with_empty_docstring():
        """"""
        pass
    
    @find_docstring(-1)
    def func_with_negative_min_length():
        """Any docstring will do."""
        pass
    
    assert func_with_empty_docstring() == False
    assert func_with_negative_min_length() == True

def test_fibonacci_closure_large_numbers():
    fib = fibonacci_closure()
    for _ in range(30):  # Get the 30th Fibonacci number
        result = fib()
    assert result == 832040  # 30th Fibonacci number

def test_function_call_counter_error_handling():
    global_dict = {}
    counter = function_call_counter(global_dict)
    
    try:
        counter['div'](1, 0)  # Division by zero
    except ZeroDivisionError:
        pass
    
    assert global_dict == {'div': 1}  # The counter should still increment

def test_flexible_function_call_counter_with_non_dict():
    create_counter = flexible_function_call_counter()
    
    try:
        create_counter(None)
    except AttributeError:
        pass
    
    try:
        create_counter([])
    except AttributeError:
        pass
