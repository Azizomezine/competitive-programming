N = int(input())
arr = []
for x in range(N):
    str = input()
    operation = str.split(' ')
    command = operation[0]

    if command == "insert":
            arr.insert(int(operation[1]), int(operation[2]))
    elif command == "print":
            print(arr)
    elif command == "remove":
            arr.remove(int(operation[1]))
    elif command == "append":
            arr.append(int(operation[1]))
    elif command == "sort":
            arr.sort()
    elif command == "pop":
            arr.pop()
    elif command == "reverse":
            arr.reverse()