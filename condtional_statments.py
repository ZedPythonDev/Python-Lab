x = int(input("Enter the number to check"))

#if x%2 == 0:
#    print(f"{x} is even")
#else:
#    print(f"{x} is odd")
#=======================================================
#          condtion presedence 
for i in range(1,x):
    if i%3==0 and i%5==0: 
        print("Hello World!")
    elif i%3==0:
        print("Hello")
    elif i%5==0:
        print("World!")
    else:
        print(f"==={i}===")
# you should have to order the condtions i%3 and i%5 have 
# to first because first i%3 excuted there is no chance for i%3 and i%5


#match instead of switch statment

y = int(input("Enter the number"))

match y:
    case 2:
        print(f"{y} is Two")
    case 3:
        print(f"{y} is Three")
    case _:
        print(f"{y} is not Two or Three")


#==============================
#Ternary condition
age =12
ticket_price = 20 if int(age)>=18 else 5
print(ticket_price)


