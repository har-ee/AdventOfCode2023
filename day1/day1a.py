import re

f = open("day1/input")

raw = f.readlines()

def find_numbers(string):
    potential = re.findall(r'\d', string)
    return int(potential[0] + potential[-1])

result = sum(map(find_numbers, raw))
print(result)
