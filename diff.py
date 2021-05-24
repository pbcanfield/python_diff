import os
from FileParser import FileParser

def compare_lists(old, new):

    last_found = 0

    removed  = {}
    inserted = {}

    for item,token in enumerate(old):
        try:
            offset_index = new.index(token ,item, len(new))
        except ValueError:
            removed[item] = token
        else:
            insertion_slice = new[last_found:offset_index]

            for index in range(last_found, offset_index):
                inserted[index] = insertion_slice[index - last_found]
            
            last_found = offset_index + 1

    insertion_slice = new[last_found:len(new)]
    for index in range(last_found, len(new)):
        inserted[index] = insertion_slice[index - last_found]

    return removed,inserted

def display_differences(i_dict, r_dict):
    
    if i_dict == {} and r_dict == {}:
        print("The files are identical.")
    else:
        print("File diffs: ")
        for line_num in i_dict:
            print('\x1b[6;30;42m+%d    %s \x1b[0m' % (line_num, i_dict[line_num]))
        
        for line_num in r_dict:
            print('\x1b[0;30;41m-%d    %s \x1b[0m' % (line_num, r_dict[line_num]))


def main(o_file, n_file):
    old = FileParser(o_file)
    new = FileParser(n_file)

    if not old.is_valid():
        return
    
    if not new.is_valid():
        return
    
    i_dict, r_dict = compare_lists(old.get_strings(), new.get_strings())
    display_differences(i_dict,r_dict)

if __name__ == '__main__':
    
    if len(os.sys.argv) == 1:
        print("Please enter either file arguments or '--help' for help.")
    else:    
        arg_one = os.sys.argv[1]

        if arg_one == '--help':
            print("Welcome to the file diff checker! Usage is simple, just enter the original ", end = '')
            print("file and the file you want to compare it to and see the differences.")
        else:
            file_one = os.sys.argv[2]
            file_two = os.sys.argv[1]

            #Arg checking.
            main(file_one, file_two)