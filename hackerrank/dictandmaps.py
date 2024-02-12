# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phone_book = {}

for _ in range(n):
    name , number = input().split()
    phone_book[name] = number

for i in range(n):
    query = input()
    if query in phone_book:
        print(query + "=" + phone_book[query] ) 
    else : 
        print("Not found")