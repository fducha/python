my_space = {'global': [None, []]}


def get(nspace, arg):
    global my_space
    if nspace is None:
        return None
    if arg in my_space[nspace][1]:
        return nspace
    return get(my_space[nspace][0], arg)


def run_command(command, nspace, arg):
    global my_space
    if command == 'add':
        my_space[nspace][1].append(arg)
    elif command == 'create':
        my_space[nspace] = [arg, []]
    elif command == 'get':
        print(get(nspace, arg))
    # print(my_space)


for i in range(int(input())):
    cmd, nsp, arg = input().split()
    run_command(cmd, nsp, arg)
