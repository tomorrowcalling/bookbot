def get_number_words(x):
    num_words = 0
    y = x.split()
    for i in y:
        num_words += 1
    return num_words

def get_num_char(x):
    d = {}
    for i in x:
        if not i.isalpha():
            pass
        elif i.lower() in d:
            d[i.lower()] += 1
        else:
            d[i.lower()] = 1
    return d

def sort_on(d):
    char_list = []
    for char, count in d.items():
        char_list.append({"char": char, "count":count})
    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list

def presentation(y, a, filepath):
    print(f"============ BOOKBOT ============ \n"
          f"Analyzing book found at {filepath}...\n"
          f"----------- Word Count ----------\n"
          f"Found {y} total words\n"
          f"--------- Character Count -------")
    for x in a:
        print(f'{x['char']}: {x['count']}')
    print("============= END ===============")








