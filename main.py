#!/usr/bin/env python3

import sys
from stats import get_num_words, count_characters, sort_characters

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def get_sort_character_count(book_text: str) -> list[dict]:
    return sort_characters(count_characters(book_text))

def create_character_string(book_text: str) -> str:
    sorted_chars = get_sort_character_count(book_text)
    char_lines = [f"{item["char"]}: {item["num"]}" for item in sorted_chars if item["char"].isalpha()]
    return "\n".join(char_lines)

def create_report(book_path: str, num_words: int, character_stats: str) -> None:
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{character_stats}
============= END ===============""")

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    
    num_words = get_num_words(book_text)
    character_stats_string = create_character_string(book_text)

    create_report(book_path, num_words, character_stats_string)

if __name__ == "__main__":
    main()

