from mnemonic import Mnemonic

mnemo = Mnemonic("english")  # инициализация класса для английского языка
with open("/Users/ivan/Desktop/Seed/mnemonic.txt", "r") as f:
    lines = f.readlines()  # чтение всех строк из файла

valid_mnemonics = []
for line in lines:
    mnemonic = line.strip()  # убираем символы переноса строки и пробелы с начала и конца строки
    if mnemo.check(mnemonic):  # проверяем мнемонику на валидность
        valid_mnemonics.append(mnemonic)

with open("/Users/ivan/Desktop/Seed/valid_mnemonic_phrases.txt", "w") as f:
    for mnemonic in valid_mnemonics:
        f.write(mnemonic + "\n")  # записываем только верные мнемоники в файл
