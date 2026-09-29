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


def sort_on(counts: tuple[str, int]) -> int:
    return counts[1]

def chars_dict_to_sorted_list(to_sort: dict[str, int]) -> list[tuple[str, int]]:
    result = []

    for char, value in to_sort.items():
        result.append((char, value))

    sorted_result = sorted(result, reverse=True, key=sort_on)

    return sorted_result