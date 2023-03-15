#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        big_num = my_list[0]
        for num in range(len(my_list)):
            if my_list[num] > big_num:
                big_num = my_list[num]
        return big_num
