Test cases for '101-lazy_matrix_mul.txt'
========================================

Import module
>>> lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

Cases to be evaluated:
----------------------

Case #1: test zero arguments
>>> lazy_matrix_mul()
Traceback (most recent call last):
...
TypeError: lazy_matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

Case #2: test None argument.
>>> lazy_matrix_mul(None, [[1, 2]])
Traceback (most recent call last):
...
TypeError: Object arrays are not currently supported

Case #3: test None argument.
>>> lazy_matrix_mul([[1, 2]], None)
Traceback (most recent call last):
...
TypeError: Object arrays are not currently supported

Case #4: test 'm_a' as an empty list
>>> lazy_matrix_mul([], [[1, 2]])
Traceback (most recent call last):
...
ValueError: shapes (0,) and (1,2) not aligned: 0 (dim 0) != 1 (dim 0)

Case #4: test 'm_b' as an empty list
>>> lazy_matrix_mul([[1, 2]], [])
Traceback (most recent call last):
...
ValueError: shapes (1,2) and (0,) not aligned: 2 (dim 1) != 0 (dim 0)

Case #5: test 'm_a' as an int list
>>> lazy_matrix_mul([1, 2], [[1, 2]])
Traceback (most recent call last):
...
ValueError: shapes (2,) and (1,2) not aligned: 2 (dim 0) != 1 (dim 0)
