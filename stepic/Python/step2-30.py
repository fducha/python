my_dict = set([input().lower() for i in range(int(input()))])
result = set()

for i in range(int(input())):
    for word in input().lower().split():
        if word not in my_dict:
            result.add(word)

print(*result, sep='\n')
