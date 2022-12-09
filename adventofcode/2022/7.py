def get_dir(dic, lst):
    if not lst:
        return dic
    for i in lst:
        if len(lst) != 1:
            return get_dir(dic[i], lst[1:])
        else:
            return dic[i]


def get_folder_size(dic, pth):
    size = 0
    path_list = pth.split('_')
    working_dir = get_dir(dic, path_list)
    for i in working_dir:
        if isinstance(working_dir[i], int):
            size += working_dir[i]
        elif isinstance(working_dir[i], dict):
            size += get_folder_size(dic, f'{pth}_{i}')
    return size


cwd = []
struct = {}
all_dirs_path = set()


for i in a:
    if i.startswith('$ cd '):
        if i == '$ cd ..':
            cwd.pop()
        else:
            currdir = i.replace('$ cd ', '')
            if currdir not in get_dir(struct, cwd):
                get_dir(struct, cwd)[currdir] = {}
            cwd.append(currdir)
            currdir_path = '_'.join(cwd)
            all_dirs_path.add(currdir_path)
    elif i == '$ ls':
        pass
    else:
        if i.startswith('dir '):
            newdir = i.replace('dir ', '')
            if newdir not in get_dir(struct, cwd):
                get_dir(struct, cwd)[newdir] = {}
                newdir_path = '_'.join(cwd + [newdir])
                all_dirs_path.add(newdir_path)
        else:
            space, filename = i.split()
            get_dir(struct, cwd)[filename] = int(space)

dirs_size = {i: get_folder_size(struct, i) for i in all_dirs_path}
ans1 = [i for _, i in dirs_size.items() if i <= 100000]
ans = sum(ans1)

# q2
all_space = get_folder_size(struct, '/')
filesystem_space = 70000000
required_space = 30000000
removing_space = all_space - (filesystem_space - required_space)
ans2 = [i for _, i in dirs_size.items() if i >= removing_space]
ans2.sort()
ans = ans2[0]
