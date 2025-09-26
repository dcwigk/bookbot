import sys
from stats import get_num_words, count_characters, sort_characters

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def get_sort_character_count(book: str) -> list[dict]:
    return sort_characters(count_characters(book))

def create_character_string(book: str) -> str:
    sort_char = get_sort_character_count(book)
    i = 0
    char_list = []
    while i < len(sort_char):
        if sort_char[i]["char"].isalpha() == False:
            i += 1
        else:
            char_list.append(f"{sort_char[i]["char"]}: {sort_char[i]["num"]}")
            i += 1
    return "\n".join(char_list)

def create_report(book: str) -> None:
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1][1:]}...
----------- Word Count ----------
Found {get_num_words(book)} total words
--------- Character Count -------
{create_character_string(book)}
============= END ===============""")

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        create_report(book)

if __name__ == "__main__":
    main()
