import functools


def find_docstring(min_length):
    """
    A closure that checks if a function has a docstring with more than the specified minimum length.
    
    Args:
    min_length (int): The minimum length of the docstring to check for.
    
    Returns:
    function: A function that takes another function as an argument and returns True if its
              docstring is longer than min_length, False otherwise.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if func.__doc__ and len(func.__doc__.strip()) > min_length:
                return True
            return False
        return wrapper
    return decorator

def fibonacci_closure():
    """
    A closure that returns the next Fibonacci number each time it's called.
    
    Returns:
    function: A function that returns the next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    def get_next_fibonacci():
        nonlocal a, b
        a, b = b, a + b
        return a
    return get_next_fibonacci

def function_call_counter(global_dict):
    """
    A closure that keeps track of how many times add/mul/div functions were called
    and updates a global dictionary with the counts.
    
    Args:
    global_dict (dict): The dictionary to update with function call counts.
    
    Returns:
    dict: A dictionary containing decorated versions of add, mul, and div functions.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            global_dict[func.__name__] = global_dict.get(func.__name__, 0) + 1
            return func(*args, **kwargs)
        return wrapper
    
    def add(a, b):
        return a + b
    
    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    return {
        'add': decorator(add),
        'mul': decorator(mul),
        'div': decorator(div)
    }

def flexible_function_call_counter():
    """
    A closure that allows passing different dictionary variables to update
    different dictionaries with function call counts.
    
    Returns:
    function: A function that takes a dictionary and returns decorated versions of add, mul, and div functions.
    """
    def create_counter(count_dict):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                count_dict[func.__name__] = count_dict.get(func.__name__, 0) + 1
                return func(*args, **kwargs)
            return wrapper
        
        def add(a, b):
            return a + b
        
        def mul(a, b):
            return a * b
        
        def div(a, b):
            return a / b
        
        return {
            'add': decorator(add),
            'mul': decorator(mul),
            'div': decorator(div)
        }
    
    return create_counter
