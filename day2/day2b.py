f = open("day2/input")

raw = f.readlines()

colours = ['red', 'green', 'blue']

def parse_round(round_str):
    colours_shown = round_str.split(',')
    colours_split = [colour_str.strip().split(' ') for colour_str in colours_shown]

    return {colour: int(num) for (num, colour) in colours_split}

def parse_game(game_str):
    id_str, rounds_str = game_str.split(':')
    _, id = id_str.split(' ')

    rounds = [parse_round(round) for round in rounds_str.split(';')]

    return int(id), rounds

def game_power(game):
    power = 1
    for colour in colours:
        power *= max([round.get(colour, 0) for round in game])
    return power

parsed = map(parse_game, raw)

result = sum([game_power(game) for _, game in parsed])
print(result)