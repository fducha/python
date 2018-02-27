string, template = input(), input()

count = 0
pos = string.find(template, 0)

while pos != -1:
    count += 1
    pos = string.find(template, pos + 1)

print(count)
