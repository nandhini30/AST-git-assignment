# List manager

def random_order(list):
    '''returns the list with random order'''
    list=[20, 50, 10,30,40]
    random_list=random.shuffle(list)
    return random_list
    
    pass

def order_by_increasing_value(list):
    '''returns the list ordered by increasing value'''
    increase_value=list.sort()'
    return increase_value
    pass

def order_by_decreasing_value(list):
    '''returns the list ordered by decreasing value'''
        decrease_value=list.sort(reverse = True)'
        return increase_value
    
    pass

def reverse_order(list):
    '''returns the list in reverse order'''
    reverse_list=list.reverse()
    return reverse_list
    
    pass

def stringfy_list(list):
    '''returns a list with all elements turned into strings'''
    string_list = [str(i) for i in list]
    return string_list
    pass

def multiply_list(list, multiple):
    '''returns the list with all elements multipled by the value multiple'''
    mult_list = [multiple*i for i in list]
    return mult_list
    pass

def get_highest_value(list):
    '''returns the highest value of the list'''
    max_value = 0
    for i in list:
        if i>max_value:
            max_value=i
    return max_value
    pass

def get_lowest_value(list):
    '''returns the lowest value of the list'''
    min_value = list[0]
    for i in list[1:]:
        if i<min_value:
            min_value=i
    return min_value
    pass

