def get_dir(dic, lst):
    for i in lst:
        if len(lst) != 1:
            return get_dir(dic[i], lst[1:])
        else:
            return dic[i]
