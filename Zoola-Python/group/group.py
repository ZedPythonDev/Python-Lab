import re

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, frequency in sorted_words:
        print(f'{word}: {frequency}')


def char_frequency(text):
    # create a dictionary to store character frequency
    char_count = {}

    # count frequency of each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # sort characters by frequency and print the first five
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for i in range(5):
        char, frequency = sorted_chars[i]
        print(f'{char}: {frequency}')

# main function


def main():
    # read text from file
    with open("C:/Users/ZoolaPy/Desktop/AI_Lab/Python-Lab/Zoola-Python/group/zoola.txt", "r") as f:
        text = f.read()

    # remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    # print word frequency
    print('Word Frequency:')
    word_frequency(text)

    # print character frequency
    print('\nCharacter Frequency:')
    char_frequency(text)

    # print statistical information
    lines = text.count('\n') + 1
    words = len(re.findall(r'\b\w+\b', text))
    chars = len(text)
    print(f'\nLines: {lines}\nWords: {words}\nCharacters: {chars}')


if __name__ == '__main__':
    main()
