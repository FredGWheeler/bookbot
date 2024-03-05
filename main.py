def main():

    book_path = "./books/frankenstein.txt"

    text = get_text(book_path)
    words = split_text(text)
    word_num = get_word_num(words)

    print(f"--- report for {book_path} --- \n\n {word_num} words found in the book \n")

    letter_count, character_count = sort_characters(count_letters(words))
    letters_by_count = sort_by_count(letter_count)
    characters_by_count = sort_by_count(character_count)
    print_letters(letters_by_count)
    #print_characters(character_count)
    print("--- End Report ---")

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
    print("Letter counts:\n")
    for letter in letters:
        count = letters[letter]
        print(f"{letter} appears {count} times")
    print("\n")
    
def print_characters(chars):
    print("Character counts:\n")
    for char in chars:
        count = chars[char]
        print(f"{char} appears {count} times")
    print("\n")

def sort_characters(characters):
    sort = dict(sorted(characters.items()))
    letters = {}
    chars = {}
    letter = False
    for c in sort:
        count = sort[c]        
        if letter == True:
            letters[c] = count
        elif c == "a":
            letters[c] = count
            letter = True
        else:
            chars[c] = count
    return letters, chars        

def sort_by_count(chars):
    sorted = {}
    while chars != {}:
        current_highest = {}
        max = float("-inf")
        for char in chars:            
            count = chars[char]
            if count > max:
                max = count
                current_highest = char
        sorted[current_highest] = max
        del chars[current_highest]
                
    return sorted


main()