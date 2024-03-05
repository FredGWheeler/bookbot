def main():

    book_path = "./books/frankenstein.txt"

    text = get_text(book_path)
    words = split_text(text)
    word_num = get_word_num(words)
    print(f"{word_num} words found in the book")

    letter_count = count_letters(words)
    print_letters(letter_count)

def get_text(book_path):
    with open(book_path) as f:
        text = f.read()
    return text
    
def split_text(text):
    words = text.split()
    return words

def get_word_num(words):
    word_num = len(words)
    return word_num

def count_letters(words):
    letters = {}
    for word in words:
        word = word.lower()
        length = len(word)
        for i in range (0, length):
            if word[i] not in letters:
                letters[word[i]] = 1
            else:
                letters[word[i]] += 1
    return letters

def print_letters(letters):
    for letter in letters:
        count = letters[letter]
        print(f"{letter} appears {count} times")

main()