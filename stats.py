def get_num_words(file_contents: str) -> int:
    return len(file_contents.split())

def count_characters(file_contents: str) -> dict:
    counter = {}
    for char in file_contents:
        lower_char = char.lower()
        if lower_char in counter:
            counter[lower_char] += 1
        else:
            counter[lower_char] = 1
    return counter

def sort_characters(count_characters: dict) -> list[dict]:
    def sort_on(items):
        return items["num"]
    char_list = []
    for char, num in count_characters.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on) 
    return char_list
