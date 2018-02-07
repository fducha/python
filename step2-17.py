def modify_list(l):
    for i in reversed(l):
        if i % 2 == 1:
            l.remove(i)
    for i in l:
        l[l.index(i)] //= 2


lst = [1, 2, 3, 4, 5, 6]

modify_list(lst)
print(lst)

modify_list(lst)
print(lst)

lst = [1, 3, 5, 7]
modify_list(lst)
print(lst)
