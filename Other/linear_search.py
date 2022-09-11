def locate_num(numbers, query):
    for i in range(0, len(numbers)):
        if(query == numbers[i]):
            return i

    return -1
