for i in range(1,100):
    if i%3==0:
        print("Hello")
    elif i%5==0:
        print("World")
    elif i%3 and i%5==0:
        print("Hello World")
    else:
        print(f"{i} is not divisible by 3 and 5")


x = int(input("enter any number "))
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case _:
        print(f'{x} not is not 1 or two ')
