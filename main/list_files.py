""" lists files in the specified path"""
import os
import sys
def list_files(path='.', reverse=False, n=1):
    """lists files in the specified path"""
    try:
        file_list = []
        for dirpath, subdirs, files in os.walk(path):
            for x in subdirs:
                file_list.append(os.path.join(dirpath, x))
            for x in files:
                file_list.append(os.path.join(dirpath, x))
    except OSError as err:
        print('OS Error: {0}'.format(err))
        return

    file_list.sort(reverse=reverse)

    for i, f in enumerate(file_list):
        if i % n != 0:
            continue
        if os.path.isfile(f):
            print(f)
        elif os.path.isdir(f):
            print(f + '/')
        elif os.path.islink(f):
            print(f + '->')
        else:
            print(f + '?')


nargs = len(sys.argv)
if nargs == 1:
    list_files()

reverse = False
n = 1
# process arguments
for arg in sys.argv[1:]:
    if arg == '-h':
        print('Usage:', sys.argv[0], '[-h -r -n <num>] [directory|file...')
    elif arg == '-r':
        reverse = True
    elif arg == '-n':
        # reset n to grab new value from the next argument
        n = 0
    elif n == 0: # -n flag must be set to view every nth file
        try:
            n = int(arg)
            if n < 1:
                print('-n argument must follow with a positive integer')
                break
        except:
            print('-n argument must follow with a positive integer')
            break
    else:
        list_files(arg, reverse, n)
