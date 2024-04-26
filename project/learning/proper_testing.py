from hypothesis import example, given
from hypothesis.strategies import integers

def my_add(a: int, b: int) -> int:
    "A customized integer addition function."
    out = a
    for _ in range(-b):
        out -= 1
    for _ in range(b):
        out += 1
    return out

# test basics
def test_add_basic() -> None:
    # Check same as slow system add
    assert my_add(10, 7) == 10 + 6
    # Check that order doesn't matter
    assert my_add(10, 7) == my_add(7, 10)

# test coverage
def test_add_naive() -> None:
    for a in range(-100, 100):
        for b in range(-100, 100):
            assert my_add(a, b) == a + b
            assert my_add(a, b) == my_add(b, a)

# randomized property checking.
@given(integers(), integers())
def test_add(a, b):
    # Check same as slow system add
    assert my_add(a, b) == a + b
    # Check that order doesn't matter
    assert my_add(a, b) == my_add(b, a)


@given(integers(), integers())
@example(5, 7)
def test_add2(a, b):
    # Check same as slow system add
    assert my_add(a, b) == a + b
    # Check that order doesn't matter
    assert my_add(a, b) == my_add(b, a)
    
def main() -> None:
    test_add_basic()
    test_add_naive()
    print(integers(min_value=0, max_value=10).example())
    

main()