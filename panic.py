phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(0)
plist.pop(2)
plist.insert(2, ' ')
plist.pop(4)
plist.insert(4, 'a')

for i in range(5): plist.pop()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
