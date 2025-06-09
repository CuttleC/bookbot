from stats import word_counter, char_counter

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    if file_contents != None:
        return file_contents
    return "no book found"

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    amount_of_words = word_counter(book_contents)
    print(f"{amount_of_words} words found in the document")
    all_chars = char_counter(book_contents)
    for character,num_occurence in all_chars.items():
        print(f"\'{character}\': {num_occurence}")

main()