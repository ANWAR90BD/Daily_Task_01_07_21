def binary_search(list, low, high, key):
    if low <= high:
        mid = (low+high) //2

        if key == list[mid]:
            return mid
        elif key > list[mid]:
            return binary_search(list, mid+1, high, key)
        else:
            return binary_search(list, low, mid+1, key)
    else:
        return - 1


data = [10, 12, 25, 45, 65, 85, 95]
print(data)

print("Found your value index number is: ",binary_search(data, 0, len(data)-1,int(input("search your numebr.. "))))


def binary_search(data, low, high, key):
    if low <= high:
        mid = (low+high) // 2
        if key == data[mid]:
            return "found here in index: ", mid
        elif key > data[mid]:
            return binary_search(data, mid+1, high, key)
        else:
            return binary_search(data, low, mid-1, key)
    else:
        return False

num = [10, 25, 56, 74, 45, 47, 20]
num.sort()
print(num)
found = binary_search(num, 0, len(num)-1, int(input("input your fonund number... ")))
print(found)