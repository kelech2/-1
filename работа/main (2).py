balance = 1000
spent = 0
while True:
    print("/n1 - Купить хлеб (50 сом)")
    print("2 - Купить молоко (80 сом)")
    print("3 - Купить шоколад (150 сом)")
    print("4 - Показать остаток денег")
    print("0 - Выйти")
    choice = input("Выберите действие:")
    if choice == "1":
        price = 50
    elif choice =="2":
        price = 80
    elif choice == "3":
        price = 150
    elif choice =="4":
        print(f"Остаток: {balance} сом")
        continue
    elif choice == "0":
         break
    else:
        print("Неверный выбор")
        continue
    if balance >= price:
        balance -= price
        spent += price
    else:
        print("Недостаточно денег")
print(f"/nВы потратили: {spent}")
print(f"Осталось: {balance}")