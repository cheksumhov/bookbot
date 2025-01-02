def main():
    path = "books/frankenstein.txt" # Path to the book file
    text = get_text(path) # Call the get_get() function, pass the path, store result in text variable
    word_count = get_word_count(text) # Call the get_word_count() function, pass text, store result in word_count
    char_count = get_char_count(text) # Call the char_count() function, pass text, stores result as a dictionary

# Print out a report of the text stats
    print(f"## Generating report of {path}. ##")
    print(f"{word_count} words found in the book.")
    for x in char_count:
        print(f"'{x}' was found {char_count[x]} times. ")
    print("## Ending report. ##")

# Takes text and returns count for each character in the form of a dictionary
def get_char_count(text):
    chars_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] = (chars_dict[char] + 1)
    return chars_dict

# Takes the text, splits by whitespace, and returns the total word count
def get_word_count(text):
    words = text.split()
    return len(words)

# Takes the path to the book, reads the file, returns the text in string format
def get_text(path):
    with open(path) as f:
        return f.read()

main()