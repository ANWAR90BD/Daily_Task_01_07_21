
def binary_search(list1, key):
    low = 0
    high = len(list1) - 1
    found = False
    while low <= high and not found:
        mid = (low+high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if found == True:
        print("found here")
    else:
        print("Not found")


list1 = [12, 23, 25, 32, 45, 5]
list1.sort()
print(list1)
key = int(input("key...."))
binary_search(list1, key)











