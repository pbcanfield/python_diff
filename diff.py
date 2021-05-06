from FileParser import FileParser

def compare_lists(old, new):

    old_index = 0
    new_index = 0
    last_old = 0
    last_new = 0 
    old_length = len(old)
    new_length = len(new)

    delete_search = False
    insert_search = False
    searching = False

    removed  = []
    inserted = []

    while True:
        if delete_search and new_index == new_length:
            delete_search = False
            new_index = last_new
            insert_search = True

        if old_index == old_length and new_index == new_length:
            break

        if old_index == old_length:
            inserted += new[old_index:new_length]
            break
            
        if new_index == new_length:
            removed += old[new_index:old_length]
            break 

        if old[old_index] == new[new_index]:
            if (not delete_search and not insert_search):
                old_index += 1
                new_index += 1

            if delete_search:
                removed += new[old_index:new_index]
                delete_search = False
            
            if insert_search:
                inserted += old[new_index:old_index]
                insert_search = False

            continue
        else:
            delete_search = True
            last_new = new_index
        

        

        if delete_search:
            new_index += 1
        
        if insert_search:
            old_index += 1

    return removed,inserted

def main(o_file, n_file):
    old = FileParser(o_file)
    new = FileParser(n_file)

    print(old.get_strings())
    print(new.get_strings())

    print(compare_lists(old.get_strings(), new.get_strings()))

if __name__ == '__main__':
    #Arg checking.
    main('old.txt', 'new.txt')