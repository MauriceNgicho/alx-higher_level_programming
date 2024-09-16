def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    
    max_val = my_list[0]  # Assum the first element is the max
    
    for num in my_list:
        if num > max_val:
            max_val = num  # Update max_val if a larger number is found
