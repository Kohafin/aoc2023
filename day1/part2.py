import re
import functools

numbers_to_digits ={
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

def get_first(line):
    number = re.search("\d|one|two|three|four|five|six|seven|eight|nine", line)[0]
    return numbers_to_digits[number]

def get_last(line):
    number =  re.search("\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line[::-1])[0][::-1]
    return numbers_to_digits[number]
def get_line_digits(line):
    first = get_first(line)
    last = get_last(line)
    digits = first + last
    print(digits)
    return int(digits)
def run(input):
    lines = input.split('\n')
    numbers = map(get_line_digits, lines)
    sum = functools.reduce(lambda a, b: a + b, numbers)
    return str(sum)


# assert run('1') == '11'
# assert run('12') == '12'
# assert run('12\n1') == '23'
# assert run('oneight') == '18'
assert run('oneight') == '18'
assert run("""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""") == '281'