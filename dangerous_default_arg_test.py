"""Module Docstring."""
import os


def some_func(arg1, arg2, arg3=[1, 2, 3], arg4=None, arg5={1,2}):
    """
    Some docstring to ensure docstring stay at its position
    """
    print("I am a function!")

    def some_other_func(arg=[1,2,3]):
        """Nested function to ensure indentation doesn't get messed up"""

        x = [1,2,3];y={1, 2, 3};z={'a': 1, 'b': 2}; t=(1, 2, 3)
        def another_nested_function(danger_one=x, danger_two=y, danger_three=z, xyz=None, safe_four=t):
            """Another deeply nested function."""
            return

        return arg

    # Returning
    return (arg1, arg2, arg3, arg4)
