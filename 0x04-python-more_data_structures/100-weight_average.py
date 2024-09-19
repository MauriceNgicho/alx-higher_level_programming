#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    #  Sum numerator and denominator
    numr = sum(score * weight for score, weight in my_list)
    denom = sum(weight for _, weight in my_list)

    return numr / denom if denom != 0 else 0
