a = input()
b = input()
if a != "красный" and a != "желтый" and a != "синий":
    print("ошибка цвета")
elif b != "красный" and b != "желтый" and b != "синий":
    print("ошибка цвета")
elif a == "красный" and b == "синий" or b == "красный" and a == "синий":
    print("фиолетовый")
elif a == "красный" and b == "желтый" or b == "желтый" and a == "красный":
    print("оранжевый")
elif a == "синий" and b == "желтый" or b == "синий" and a == "желтый":
    print("зеленый")
elif a == "красный" and b == "красный":
    print("красный")
elif a == "желтый" and b == "желтый":
    print("желтый")
elif a == "синий" and b == "синий":
    print(синий)