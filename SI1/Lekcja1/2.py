print("Podaj swoje imie i nazwisko")
nazwa = input()
print(nazwa)

imie, nazwisko = nazwa.split(" ")

y = len(imie)

print('Ilosc znakow w imieniu:', y)
print('Nazwisko malymi literami: ', nazwisko.lower())