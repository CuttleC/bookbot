def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    if file_contents != None:
        return file_contents
    return "no book found"

def word_counter(book_text):
    book_words = book_text.split()
    return len(book_words)

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    amount_of_words = word_counter(book_contents)
    print(f"{amount_of_words} words found in the document")

main()