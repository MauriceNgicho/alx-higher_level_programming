#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            # Try to divide elements from both lists
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            # If either list is too short
            print("out of range")
            result = 0
        except TypeError:
            # If an element is not a number
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            # If division by zero occurs
            print("division by 0")
            result = 0
        finally:
            # Append the result to the new list
            new_list.append(result)
    return new_list
