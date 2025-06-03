def word_counter(book_text):
    book_words = book_text.split()
    return len(book_words)

def char_counter(book_text):
    all_chars = {}
    
    for character in book_text:
        lower_character = character.lower()
        if lower_character in all_chars:
            all_chars[lower_character] += 1
        else:
            all_chars[lower_character] = 1
    
    return all_chars