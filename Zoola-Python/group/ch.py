def count_char_frequency(s):
    char_freq = {}
    for i in s:
        if i in char_freq:
            char_freq[i] += 1
        else:
            char_freq[i] = 1
    sorted_char_freq = dict(
        sorted(char_freq.items(), key=lambda x: x[1], reverse=True))
    print("Character frequency:")
    for i, j in sorted_char_freq.items():
        print(i + " : " + str(j))
    print("\nTop five characters with highest frequency:")
    count = 0
    for i, j in sorted_char_freq.items():
        if count == 5:
            break
        print(i + " : " + str(j))
        count += 1


# test
s = "This is a test string to count character frequency."

count_char_frequency(s)
