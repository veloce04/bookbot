def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowercase_text = text.lower()
    get_chars_dict = character_count(lowercase_text)
    chars_sorted_list = chars_dict_to_sorted_list(get_chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for char in chars_sorted_list:
        if not char["char"].isalpha():
            continue
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    
    print("--- End report ---")
    

    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def character_count(string):
    chars = {}
    for c in string:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
            

main()