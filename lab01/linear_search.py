items = [8, 9 ,10, -1]

x = int(input("Enter a number: "))
# found = False
for index, item in enumerate(items):
    if x == item:
        found = True
        print("Found it")
        print(index)
        break # find one
else:
# if not found: (= if True)
    print("Not found")
