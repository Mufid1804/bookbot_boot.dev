def main():
    book_path = "books/frankenstein.txt"
    book = Book(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book.word_count} words found in the document\n")

    char_counts = book.char_freq
    sorted_char_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_char_counts:
        print(f"The '{char}' char was found {count} times")

    print("--- End report ---")


class Book:
    def __init__(self, path):
        self.path = path
        self.text_content = self._read_book()
        self.word_count = self._count_words()
        self.char_freq = self._get_char_freq()

    def _read_book(self):
        with open(self.path) as f:
            return f.read()

    def _count_words(self):
        return len(self.text_content.split())

    def _get_char_freq(self):
        char_counts = {}
        for char in self.text_content.lower():
            if char.isalpha():
                char_counts[char] = char_counts.get(char, 0) + 1
        return char_counts


if __name__ == "__main__":
    main()
