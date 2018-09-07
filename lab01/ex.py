no_list = [4, 3, 25, -4, 0 ,5, 45]
number = input("Please input a number ")
if number in no_list:
    print(number, "is in the list")
    no_list[x] = number
    print("Number is at position ", x+1)
else:
    print("Number is not in the list")