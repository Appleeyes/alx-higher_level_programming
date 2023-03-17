#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    prev = [roman_dict[x] for x in roman_dict]
    result = 0

    for letter in range(len(prev)):
        result += prev[letter]
        if prev[letter - 1] < result[letter] and letter != 0:
            result -= (prev[letter -1] + prev[letter - 1])
    return result
