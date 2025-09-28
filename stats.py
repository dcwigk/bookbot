def get_num_words(file_contents: str) -> int:
    return len(file_contents.split())


def count_characters(file_contents: str) -> dict:
    counter = {}
    for char in file_contents.lower():
        counter[char] = counter.get(char, 0) + 1
    return counter


def sort_characters(character_counts: dict) -> list[dict]:
    char_list = []
    for char, num in character_counts.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list
