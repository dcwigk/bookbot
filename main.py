from stats import get_num_words, count_characters

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    
def main() -> None:
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    print(count_characters(book))

if __name__ == "__main__":
    main()
