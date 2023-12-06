ELF_QUERY = {'red': 12, 'green': 13, 'blue': 14}

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
    return dict

def analyze_game(line):
    column_separated = line.split(': ')
    game_id = get_game_id(column_separated[0])
    game = column_separated[1]
    subsets = get_subsets(game)
    return [game_id, analayze_subsets(subsets)]


def run(input):
    lines = input.split('\n')
    games = map(analyze_game, lines)
    valid_games_sum = 0
    for game in games:
        game_id = game[0]
        game_dict = game[1]
        valid = True
        for color in game_dict:
            if game_dict[color] > ELF_QUERY[color]:
                valid = False
        if valid:
            valid_games_sum += game_id
    return str(valid_games_sum)

# assert get_game_id("Game 1") == 1
# assert get_subsets("red 1, green 2; blue 3") == ["red 1, green 2", "blue 3"]
# assert analayze_subsets(["red 1, green 2", "blue 3"]) == {'red': 1, 'green': 2, 'blue': 3}
# assert analyze_game("Game 1: red 1, green 2; blue 3") == [1, {'red': 1, 'green': 2, 'blue': 3}]
# assert run("Game 1: red 1, green 2; blue 3\nGame 2: red 1\nGame 3: red 1000, blue 2, green 1") == 3
# assert run("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""") == 8