def solution(phone_book): 
    my_dict = dict()
    for phone in phone_book:
        value = ''
        for i in phone:
            value += i
            if my_dict.get(value):
                my_dict[value] += 1
            else:
                my_dict[value] = 1
    for phone in phone_book:
        if my_dict[phone] >= 2:
            return False
    return True