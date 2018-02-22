import os.path


def is_python_file(file_name):
    return file_name[-3::] == '.py'


py_dirs = []
for cur_dir, dir, files in os.walk('main/'):
    for f in files:
        if is_python_file(f):
            py_dirs.append(cur_dir)
            break

with open('step18_result.txt', 'w') as res:
    print(*sorted(py_dirs), sep='\n', file=res)

