from stats import get_num_words, count_characters, sort_characters

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    
def main() -> None:
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    num_char = count_characters(book)
    print(f"Found {num_words} total words")
    print(sort_characters(num_char))

if __name__ == "__main__":
    main()
