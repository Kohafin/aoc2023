import functools
# FIND THE MINIMUM VAIABLE NUM OF CUBES FROM EACH GAME AND MULTIPLY THEM TOGETHER

def get_game_id(game_name):
    game_id = game_name.split(' ')[1]
    return int(game_id)

def get_subsets(game):
    subsets = game.split('; ')
    return subsets

def analayze_subsets(subsets):
    dict = {'red': 0, 'green': 0, 'blue': 0}
    for subset in subsets:
        for cube in subset.split(', '):
            count, color = cube.split(' ')
            count = int(count)
            if (dict[color] < count):
                dict[color] = count
    return functools.reduce(lambda a, b: a*b, dict.values())

def analyze_game(line):
    column_separated = line.split(': ')
    game_id = get_game_id(column_separated[0])
    game = column_separated[1]
    subsets = get_subsets(game)
    return analayze_subsets(subsets)


def run(input):
    lines = input.split('\n')
    games = map(analyze_game, lines)
    sum_of_powers = functools.reduce(lambda a, b: a+b, games)
    return str(sum_of_powers)

assert get_game_id("Game 1") == 1
assert get_subsets("1 red, 2 green; 3 blue") == ["1 red, 2 green", "3 blue"]
assert analayze_subsets(["1 red, 2 green", "3 blue"]) == 6
assert analyze_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48
assert analyze_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 12
assert analyze_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == 1560
assert analyze_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 630
assert analyze_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == 36
assert run("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""") == '2286'