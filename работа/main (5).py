data_tuple = ('h', 6.13, 'C', ['e', 'T'], True, 'k', 'e', '3', 'e', 1, ('g', 'x'), False)
letters = []
numbers = []

def split(items):
    for item in items:
        if isinstance(item, (list, tuple)):
            split(item)
        elif isinstance(item, bool):
            letters.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
        elif isinstance(item, str):
            if item.isdigit():
                numbers.append(int(item))
            else:
                letters.append(item)
split(data_tuple)
print(letters)
print(numbers)

if 6.13 in numbers:
    numbers.remove(6.13)
bools = [x for x in letters if isinstance(x, bool)]
letters = [x for x in letters if not isinstance(x, bool)] + bools

i3 = numbers.index(3)
i1 = numbers.index(1)
numbers.insert(min(i3, i1) + 1, 2)
print(numbers)

numbers.sort(reverse=True)
letters = letters[::-1]
letters = [x.swapcase() if isinstance(x, str) else x for x in letters]
print(numbers)
print(letters)

target = "Cheetah"
pool = [x.lower() for x in letters if isinstance(x, str)]
bools = [x for x in letters if isinstance(x, bool)]

word = []
for ch in target:
    if ch.lower() in pool:
        word.append(ch)
    else:
        word.append(ch)
        pool.append(ch.lower())
        print(f"Добавлена недостающие буква: {ch}")

letters = word + bools
print(letters)
print("".join(x for x in letters if isinstance(x, str)))