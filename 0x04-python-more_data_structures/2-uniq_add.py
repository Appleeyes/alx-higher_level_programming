#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = {x for x in my_list}
    return sum(unique)
