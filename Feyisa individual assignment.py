string = input("Enter any string ")
feye={}
for char in string:
    if char in feye:
        feye[char]+= 1
    else:
        feye[char]= 1
print("character frequency is:\n"+ str(feye))
    