#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numr = sum(score * weight for score, weight in my_list) #  Sums the numnerator
    denom = sum(weight for _, weight in my_list) #  Sums the denominator

    return numr / denom if denom != 0 else 0
