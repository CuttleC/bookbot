import sys
from stats import word_counter, char_counter, char_count_sorter

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    if file_contents != None:
        return file_contents
    return "no book found"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    source_book = sys.argv[1]
    book_contents = get_book_text(source_book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {source_book}...")
    print("----------- Word Count ----------")
    
    amount_of_words = word_counter(book_contents)
    print(f"Found {amount_of_words} total words")

    print("--------- Character Count -------")

    all_chars = char_counter(book_contents)
    sorted_all_chars = char_count_sorter(all_chars)

    for character in sorted_all_chars:
        if not character["char"].isalpha():
            continue
        print(f"{character["char"]}: {character["num"]}")
    
    print("============= END ===============")

main()