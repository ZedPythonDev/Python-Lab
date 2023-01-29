# file name
file_name = "C:/Users/ZoolaPy/Desktop/Zoola-Python/group/zoola.txt"


def remove_special_characters(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~፤።፣+፨='''
    for char_element in string:
        if char_element in punctuations:
            string = string.replace(char_element, "")
    return string

# reading from file and removing special character


def validate_file(filename):
    try:
        with open(filename, 'r', encoding="utf8") as f:
            data = f.read()
        with open(filename, "w+", encoding="utf8") as f:
            f.write(remove_special_characters(data))
    except FileNotFoundError:
        print("File not found")


def characters_frequency(my_file):
    characters_freq = {}
    for i in my_file:
        if i in characters_freq:
            characters_freq[i] += 1
        else:
            characters_freq[i] = 1
    sorted_char_freq = dict(
        sorted(characters_freq.items(), key=lambda x: x[1], reverse=True))
    # To print all characters frequency
    #print("Character frequency:")
    # for i, j in sorted_char_freq.items():
    #print(i + " : " + str(j))
    print("================================================")
    print("Top five characters with highest frequency:")
    print("================================================")
    count = 0
    for key, value in sorted_char_freq.items():
        if count == 5:
            break
        if key == " ":
            print("Space :" + str(value))
        else:
            print(key + " : " + str(value))
        count += 1
    print()

# Counting Word frequecies


def word_frequency(text):
    word_freq = {}
    words = text.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_word_freq = dict(
        sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    print("\n===================")
    print("Word frequency:")
    print("====================")
    for word, freq in sorted_word_freq.items():
        print(word + " : " + str(freq))

# Main function


def main():
    validate_file(file_name)
    # read text from file
    with open(file_name, "r", encoding="utf8") as f:
        text = f.read()
    # print word frequency
    word_frequency(text)
    # print character frequency
    characters_frequency(text)
    # print statistical information
    lines = text.split("\n")
    number_of_line = len(lines)
    number_of_word = len(text.split())
    number_of_characters = len(text) - text.count(' ')
    print("=====================================")
    print("Total Number of Line: ", number_of_line)
    print("Total Number of Word: ", number_of_word)
    print("Total Numbers of Characters: ", number_of_characters)
    print("=====================================")
    print()


# calling main function
if __name__ == '__main__':
    main()
