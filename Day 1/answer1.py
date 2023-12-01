import re
def extract_first_digits(input_string):
    left_digit_match = re.search(r'\d', input_string)
    left_digit = left_digit_match.group() if left_digit_match else None

    right_digit_match = re.search(r'\d', input_string[::-1])
    right_digit = right_digit_match.group() if right_digit_match else None

    # print(left_digit, end=", ")
    # print(right_digit)
    return int(left_digit), int(right_digit)

file_path = 'challenge1.txt'
sum = 0
with open(file_path, 'r') as file:
    for line in file:
        x = line.strip()
        left_digit, right_digit = extract_first_digits(x)
        sum += ((left_digit*10) +right_digit)

print(sum)