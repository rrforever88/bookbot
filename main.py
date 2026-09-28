def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def word_count(string):
    words = string.split()
    count = len(words)

    print(f"Found {count} total words")

def main():
    book_text = get_book_text("books/frankenstein.txt")

    print(get_book_text("books/frankenstein.txt"))
    word_count(book_text)

main()