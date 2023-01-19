'''specialCharacters = !()-[]{}; : '"\,<>./?@#$%^&*_~

my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
   if char not in specialCharacters:
       no_punct = no_punct + char
print(no_punct)
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
        print(f"{char}: {frequency}")'''

def count_word_frequency(text):
    word_freq = {}
    words = text.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_word_freq = dict(
        sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    print("Word frequency:")
    for word, freq in sorted_word_freq.items():
        print(word + " : " + str(freq))
# test
text = "This is a test string to count word frequency. This string contains multiple words and multiple instances of the same word."
count_word_frequency(text)
