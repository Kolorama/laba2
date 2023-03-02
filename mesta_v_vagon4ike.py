x = int(input("Введите номер места"))
print()
if x > 36:
    print("Боковое")
elif x % 2:
    print("Купе снизу")
else:
    print("Купе сверху")