from stats import word_count, char_count, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def print_report(path, word_count, sorted_list):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        if i[0].isalpha():
            print(f"{i[0]}: {i[1]}")

    print("============= END ===============")


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)

    get_chars = char_count(book_text)

    words = word_count(book_text)

    sorted_chars = chars_dict_to_sorted_list(get_chars)
    print_report(book_path, words, sorted_chars)


main()