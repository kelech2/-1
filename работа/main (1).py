import random
secret = random.randint(1,100)
attempts = 7
while attempts > 0:
    guess = int(input("Введите число:"))
    attempts -= 1
    if guess < secret:
        print("Загаданное число больше")
    elif guess > secret:
        print("Загаданное число меньше")
    else:
        print("Вы победили!")
        break
    if attempts == 0:
        print("Вы проиграли.")
        print(f"Загаданное число: {secret}")