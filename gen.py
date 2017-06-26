def simple_generator():
    yield 1
    yield 2
    yield 3

ex_gen = simple_generator()
print next(ex_gen)
print next(ex_gen)
print next(ex_gen)