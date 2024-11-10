
from typing import Iterable, Callable

def ft_filter(function: Callable, iterable: Iterable) -> Iterable:
    '''
    A copy of the official filter() function
    '''
    return [x for x in iterable if function(x)]
