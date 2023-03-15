#!/usr/bin/python3
def multiple_returns(sentence):
    the_length = len(sentence)
    char1 = sentence[0] if the_length > 0 else None
    return (the_length, char1)
