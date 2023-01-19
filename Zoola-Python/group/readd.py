import re


def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)  # remove special characters
    text = text.lower()  # convert to lowercase
    return text


def read_file_and_clean(filepath):
    with open(filepath, "r") as f:
        text = f.read()
        cleaned_text = clean_text(text)
    return cleaned_text


cleaned_text = read_file_and_clean("C:/Users/ZoolaPy/Desktop/AI_Lab/Python-Lab/Zoola-Python/group/zoola.txt")
words = cleaned_text.split()
print(words)


def count_line_word_char(s):
    lines = s.split("\n")
    line_count = len(lines)
    word_count = len(s.split())
    char_count = len(s)
    print("Line count: ", line_count)
    print("Word count: ", word_count)
    print("Character count: ", char_count)


# test
s = "This is a test string.\nIt has multiple lines, words, and characters."
count_line_word_char(s)
