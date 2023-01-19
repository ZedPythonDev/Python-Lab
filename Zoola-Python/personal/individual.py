# Python Program to Convert Roman Numbers to Integer
# with validation by ZoolaPython(Zeleke Zerihun)
print("Zeleke Zerihun ID DBUR/1106/12")


def IsRoman(ch):
    if (ch in ['I', 'V', 'X', 'L', 'C', 'D', 'M']):
        return 1
    return -1


def RomanValue(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def romanToDecimal(roman_number):

    result = 0
    counter = 0
    while (counter < len(roman_number)):
        check = IsRoman(roman_number[counter])
        if (check == 1):
            str1 = RomanValue(roman_number[counter])
            if (counter + 1 < len(roman_number)):

                str2 = RomanValue(roman_number[counter + 1])

                if (str1 >= str2):
                    result = result + str1
                    counter = counter + 1
                else:
                    result = result + str2 - str1
                    counter = counter + 2
            else:
                result = result + str1
                counter = counter + 1
        else:
            return -1
    return result


print()
roman = input("Please Enter Roman Number to Convert to Decimal : ")
print()
print("-------------------------------")
print("Roman to Integer Conversion")
if (romanToDecimal(roman.upper()) > -1):
    print(f"{roman.upper()} = " + str(romanToDecimal(roman.upper())))
else:
    print(f"{roman.upper()} is Not Roman Number")
print("-------------------------------")
print()
