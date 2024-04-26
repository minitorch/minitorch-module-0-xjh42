from typing import Callable, Iterable

def add(a: float, b: float) -> float:
    return a + b

def mul(a: float, b: float) -> float:
    return a * b

# pass function as arguments
def combine3(
    fn: Callable[[float, float], float],
    a: float,
    b: float,
    c: float
) -> float:
    return fn(fn(a, b), c)

# return function value
def ret_combine3(
    fn: Callable[[float, float], float]
) -> Callable[[float, float, float], float]:
    def new_fn(a: float, b: float, c: float) -> float:
        return fn(fn(a, b), c)
    return new_fn

# define a filter function
def filter(fn: Callable[[float], bool]) -> Callable[[Iterable[float]], Iterable[float]]:
    def apply(arr: Iterable[float]) -> Iterable[float]:
        ret = []
        for x in arr:
            if fn(x):
                ret.append(x)
        return ret
    return apply

def more_than_5(x: float) -> bool:
    return x > 5.0

def main() -> None:
    add_v: Callable[[float, float], float] = add
    print(add_v(1, 2))
    
    mul_v: Callable[[float, float], float] = mul
    print(mul_v(1, 2))
    
    print(combine3(add_v, 1, 2, 3))
    
    combine_fn = ret_combine3(add_v)
    print(combine_fn(1, 2, 3))
    
    # test filter function
    filter_more_than_5 = filter(more_than_5)
    print(filter_more_than_5([1, 3, 5, 6, 9, 10]))
    

main()