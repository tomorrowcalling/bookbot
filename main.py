from stats import get_number_words, get_num_char, sort_on, presentation
import sys
filepath = ''

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        string = f.read()
        return string

def main ():
    x = get_book_text(filepath)
    y = get_number_words(x)
    z = get_num_char(x)
    a = sort_on(z)
    presentation(y, a, filepath)


main()
