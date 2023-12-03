f = open("day2/input")

raw = f.readlines()

max_values = {'red': 12, 'green': 13, 'blue': 14}

def parse_round(round_str):
    colours_shown = round_str.split(',')
    colours_split = [colour_str.strip().split(' ') for colour_str in colours_shown]

    return {colour: int(num) for (num, colour) in colours_split}

def parse_game(game_str):
    id_str, rounds_str = game_str.split(':')
    _, id = id_str.split(' ')

    rounds = [parse_round(round) for round in rounds_str.split(';')]

    return int(id), rounds

def valid_round(round):
    return all(round[colour] <= max_values[colour] for colour in round)

def valid_game(game):
    return all(valid_round(round) for round in game)

parsed = map(parse_game, raw)
result = sum([id for id, game in parsed if valid_game(game)])

print(result)