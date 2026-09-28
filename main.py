from stats import word_count, char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")

    print(get_book_text("books/frankenstein.txt"))
    word_count(book_text)
    get_chars = char_count(book_text)
    print(get_chars)

main()