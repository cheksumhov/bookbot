def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    print(word_count)

def get_word_count(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

main()