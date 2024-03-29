def solution(s):
    answer = 0
    NUMBERS = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }
    for number in NUMBERS.keys():
        if number in s:
            s = s.replace(number, NUMBERS[number])
    return int(s)

print(solution("one4seveneight"))