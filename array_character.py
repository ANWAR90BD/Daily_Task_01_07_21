def binary_search(data, low, high, key):
    if low <= high:
        mid = (low+high) // 2
        if key == data[mid]:
            return "Your are found: ", key, "here index is: ",mid
        elif key > data[mid]:
            return binary_search(data, mid+1, high, key)
        else:
            return binary_search(data, low, mid-1, key)
    else:
        return "Your are found: ", key, "this is not found your array "

array = ["Anwar", "Masud", 'Sopon', "Tanvir", "Tanin"]
array.sort()
found = binary_search(array, 0, len(array)-1, "Anwar")
print(found)

found = binary_search(array, 0, len(array)-1, "aman")
print(found)