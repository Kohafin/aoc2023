import re
import functools
def get_line_digits(line):
    first = re.search("\d", line)[0]
    last = re.search("\d", line[::-1])[0]
    digits = first + last
    return int(digits)
def run(input):
    lines = input.split('\n')
    numbers = map(get_line_digits, lines)
    sum = functools.reduce(lambda a, b: a + b, numbers)
    return str(sum)

assert run('1') == '11'
assert run('12') == '12'
assert run('12\n1') == '23'


