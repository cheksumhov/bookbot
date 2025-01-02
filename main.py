def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    print(word_count)

# Function to take the text and return count for each character

# Take the text, split by whitespace, and return the length
def get_word_count(text):
    words = text.split()
    return len(words)

# Take the path to the book, read the fiel, and return the text
def get_text(path):
    with open(path) as f:
        return f.read()

main()