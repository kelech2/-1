n = int(input("Сколько температур введёте?"))
temps = []
for i in range(n):
    t = float(input(f"Температура {i + 1}:"))
    temps.append(t)
average = sum(temps) / len(temps)
print(f"Средняя температур на сегедня составляет {average:.1f} град цельсия")