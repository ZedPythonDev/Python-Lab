def char_frequency(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
string = input("Enter String : ")
print(char_frequency(string))