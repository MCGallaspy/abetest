# What is this?

A collection of scripts for automatically grading students' Python homework.
The basic idea is this:

1. Student creates an `answers` module.
2. The module is run against a `unittest` test suite. (In a sandboxed environment!)
3. The # of successful tests / total tests is the grade.

There are three files:

1. `tester.py`. Running this module grades the provided `answers` module.
2. `answers_template.py` with stubbed out functions that have instructions in their docstring.
3. `answers.py` which contains possible implementations of the functions.

# Potential problems (and a solution)

It's possible that test requirements might be written in such a way that a student can avoid meeting them in spirit
while still technically passing. For instance, consider a fucntion that *requires* the student to perform some
action in a loop -- for example decrementing an `int` until it reaches `0`. If you only check that the `int` is 
equal to `0` when the function returns, then a student could just set it directly to `0`.

In this case a solution is to use `unittest.Mock` to make assertions about which special methods are called, like
`__sub__` or `__gt__`. There is an example of this in `tester.py`. Essentially this allows us to somewhat easily
make assertions about the actual *code* that was written, and not just the results that it had.

# Remarks

Tested with Python 3.5.