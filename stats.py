def word_count(string):
    words = string.split()
    count = len(words)

    print(f"Found {count} total words")

def char_count(string: str) -> dict[str, int]:
    count_char = {}

    chars = string.lower()

    for char in chars:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1

    return count_char
