def menu_v1(lst):
    while True:
        print("1. Show")
        print("2. Max")
        print("3. Min")
        print("4. Get")
        print("5. Delete")
        print("0. Exit")
        
        c = input("Choice: ")
        
        if c == "1":
            print(lst)
        elif c == "2":
            print(max(lst))
        elif c == "3":
            print(min(lst))
        elif c == "4":
            i = int(input("Index: "))
            print(lst[i])
        elif c == "5":
            i = int(input("Index: "))
            lst.pop(i)
        elif c == "0":
            break

def menu_v2(lst):
    while True:
        print("1. Show")
        print("2. Max")
        print("3. Min")
        print("4. Get")
        print("5. Delete")
        print("0. Exit")
        
        c = input("Choice: ")
        
        if c == "1":
            print(lst)
        elif c == "2":
            try:
                if len(lst) > 0:
                    print(max(lst))
                else:
                    print("Empty")
            except:
                print("Error")
        elif c == "3":
            try:
                if len(lst) > 0:
                    print(min(lst))
                else:
                    print("Empty")
            except:
                print("Error")
        elif c == "4":
            try:
                i = int(input("Index: "))
                print(lst[i])
            except:
                print("Error")
        elif c == "5":
            try:
                i = int(input("Index: "))
                lst.pop(i)
            except:
                print("Error")
        elif c == "0":
            break
        else:
            print("Error")

nums = []
while True:
    try:
        n = int(input("Number: "))
        if n == 0:
            break
        nums.append(n)
    except:
        print("Error")

print("V1:")
try:
    menu_v1(nums.copy())
except:
    print("Error")

print()
print("V2:")
menu_v2(nums.copy())
