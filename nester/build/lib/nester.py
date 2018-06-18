def print_lol(each_list):
    for item in each_list:
        if isinstance(item,list):
            print_lol(item)
        else:
            print(item)

