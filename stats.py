def word_counter(book_text):
    book_words = book_text.split()
    return len(book_words)

def char_counter(book_text):
    # for each char in book_text
    # check if it's in our dictionary already
    # if so, increase its count by 1
    # otherwise add it to the dictionary with the number 1
    # return the dictionary