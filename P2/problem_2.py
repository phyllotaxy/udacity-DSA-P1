from os.path import isdir, isfile, join
from os import listdir

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    all_paths = list()
    walk(all_paths, suffix, path)
    return all_paths

def walk(path_list, suffix, path):
    """
    Put the paths of all files with given suffix beneath path into a list.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path under which files with the given suffix should be searched
      path_list(list): list that contains all the files with given suffix that have been seen so far

    Returns:
       Nothing.
    """
    if isdir(path):
        for sub_path in listdir(path=path):
            # Join path with all the paths in the subdirectories
            joined_path = join(path, sub_path)
            # base case
            # if path is a file, check suffix
            if isfile(joined_path) and sub_path.endswith(suffix):
                path_list.append(joined_path)
            # induction step
            # If path is again a directory, call function recursively.
            elif isdir(joined_path):
                walk(path_list, suffix, joined_path)

def main():
    tc_1()
    tc_2()
    tc_3()
    tc_4()

# tests

# path not existent
def tc_1():
    all_paths = find_files('.c', 'a*7dfs25&jn')
    for path in all_paths:
        print(path)     # all_paths empty, print statement not executed

# testdir downloaded from udacity site
def tc_2():
    all_paths = find_files('.c', './testdir')
    for path in all_paths:
        print(path)
    # prints
    # ./testdir/subdir3/subsubdir1/b.c
    # ./testdir/t1.c
    # ./testdir/subdir5/a.c
    # ./testdir/subdir1/a.c

# empty folder
def tc_3():
    all_paths = find_files('.c', './testdir_1')
    for path in all_paths:
        print(path)     # all_paths empty, print statement not executed

# long nested directories
def tc_4():
    all_paths = find_files('.c', './testdir_2')
    for path in all_paths:
        print(path)
    # prints
    # ./testdir_2/a.c
    # ./testdir_2/L1/b.c
    # ./testdir_2/L1/L2/c.c
    # ./testdir_2/L1/L2/L3/d.c
    # ./testdir_2/L1/L2/L3/L4/e.c
    # ./testdir_2/L1/L2/L3/L4/L5/f.c

if __name__ == '__main__':
    main()
