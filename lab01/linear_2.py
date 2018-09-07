items = [4, 6 ,7 ,8, -54, 23]
x = int(input("Enter a number "))

if x in items:
    print("found")
    found_index = items.index(x)
    print(found_index+1)
else:
    print("not found")


#binary search:
#organised list
#log2(n)

#pip install pymongo