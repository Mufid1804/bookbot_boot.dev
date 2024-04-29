def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document\n")

    char_counts = get_char_counts(text)
    sorted_char_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def read_book(book_path):
    with open(book_path) as f:
        return f.read()


def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


def count_words(text):
    return len(text.split())


if __name__ == "__main__":
    main()