import regex as re

f = open("day1/input")

raw = f.readlines()

number_mappings = {
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9"
}

number_pattern = r'\d|' + '|'.join(number_mappings.keys())

def find_numbers(string):
    matches = re.findall(number_pattern, string, overlapped=True)
    numbers = [number_mappings.get(num, num) for num in matches]
    return int(numbers[0] + numbers[-1])

result = sum(map(find_numbers, raw))
print(result)
