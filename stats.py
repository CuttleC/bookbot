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

def char_count_sorter(all_chars):
    sorted_chars = []
    
    for character,num_occurence in all_chars.items():
        temp = {"char":character, "num":num_occurence}
        sorted_chars.append(temp)
    
    sorted_chars.sort(reverse=True,key=num_comparer)
    return sorted_chars

def num_comparer(char_dict):
    return char_dict["num"]