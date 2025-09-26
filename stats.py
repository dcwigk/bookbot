def get_num_words(file_contents: str) -> int:
    return len(file_contents.split())

def count_characters(file_contents: str) -> dict:
    counter = {}
    for char in file_contents:
        lower_char = char.lower()
        if lower_char in counter:
            counter[lower_char] += 1
            continue
        counter[lower_char] = 1
    return counter
