import re

def word_to_digit(word):
    word_to_digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    return word_to_digit_mapping.get(word.lower(), word)


def find_first_digit_or_word(string):
    left_match = re.search(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)', string, re.IGNORECASE)

    right_match = None
    for match in re.finditer(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)', string, re.IGNORECASE):
        right_match = match

    if left_match:
        left_result = word_to_digit(left_match.group(0))
        left_index = left_match.start()
    else:
        left_result = left_index = None

    if right_match:
        right_result = word_to_digit(right_match.group(0))
        right_index = len(string) - right_match.end() - 1
    else:
        right_result = right_index = None

    return int(left_result), left_index, int(right_result), right_index

def replace_middle_letter(match):
    word = match.group(0)
    return word[0] + word_to_digit(word) + word[-1]

def replace_middle_letters(string):
    updated_string = re.sub(r'(?:one|two|three|four|five|six|seven|eight|nine)', replace_middle_letter, string, flags=re.IGNORECASE)
    return updated_string




file_path = 'challenge2.txt'
sum = 0
with open(file_path, 'r') as file:
    lines = file.readlines()

with open(file_path, 'w') as file:
    for line in lines:
        x = line.strip()
        new_string = replace_middle_letters(x)
        new_string = replace_middle_letters(new_string)
        file.write(new_string + "\n")

with open(file_path, 'r') as file:
    for line in file:
        x = line.strip()
        # print(x)

        left_result, left_index, right_result, right_index = find_first_digit_or_word(x)

        # print("Left:  Result:", left_result, "Right: Result:", right_result)

        sum += ((left_result*10) +right_result)

print(sum)








