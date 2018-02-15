# -*- coding: utf-8 -*-

word = "бутылок"
count_bottles = int(input("Про сколько бутылок пива спеть??\n"))
for beer_num in range(count_bottles, 0, -1):
    print(beer_num, word, " пива на столе!!")
    print(beer_num, word, " пива!!")
    print("Возьми одну!!")
    print("Пусти по кругу!!")
    if beer_num == 1:
        print("Нет больше пива на столе!!")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "бутылка"
        elif new_num > 1 and new_num < 5:
            word = "бутылки"
        else:
            word = "бутылок"
        print(new_num, word, " пива на столе!!")
    print()
