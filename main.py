def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    chars_dict = get_chars_dict(book_text)
    sorted_char_dicts_list = get_sorted_char_dicts_list(chars_dict)
    print_report(book_path, word_count, sorted_char_dicts_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())
    

def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        lower_case_char = char.lower()
        if lower_case_char in chars_dict:
            chars_dict[lower_case_char] += 1
        else:
            chars_dict[lower_case_char] = 1
    return chars_dict


def print_report(book_path, word_count, sorted_char_dicts_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char_dict in sorted_char_dicts_list:
        if char_dict["char"].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")

def get_sorted_char_dicts_list(chars_dict):
    char_dicts_list = []
    for char in chars_dict:
        char_dicts_list.append({"char": char, "num": chars_dict[char]})
    char_dicts_list.sort(reverse=True, key=sort_on)
    return char_dicts_list


def sort_on(d):
    return d["num"]


main()
