
#----------------- Name PAWLOS BEZIE Id 0189/12 --------------------

def roman_To_Decimal(roman):
    roman_number_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal = 0
    prev_value = 0
    l=v=d=0
    k = 4
    current_char, count = None, 0
    for ch in reversed(roman):
        if ch == current_char:
                count += 1
        else:
                current_char,count = ch,1
        if count == k:
                return print("It can not be more than 3 Consecutive ")
        if(ch=='L'):
            l+=1
        if(ch=='V'):
            v+=1
        if(ch=='D'):
            d+=1
  
    if(l<2 and v<2 and d<2):
       pass
    else:
        return print("V,L, and D can not be repeated. ")
    
    for char in reversed(roman): 
        current_value = roman_number_values[char]
        if current_value >= prev_value:
            decimal += current_value     
        else:   
            decimal -= current_value
        prev_value = current_value
    print(decimal)


try:
    for i in range(5):
        n=input("Enter the Roman numeral: ")
        roman_To_Decimal(n.upper())
except:
    print("The input is wrong. Please try again")