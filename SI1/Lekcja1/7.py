import csv
import pandas as pd


def showcolumn():
    print("Podaj numer kolumny do wyświetlenia")
    colnum = input()
    with open('plik.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            print(row[int(colnum)])


def datatype():
    print("Podaj numer kolumny której chcez znać typ danych")
    colnum = input()
    with open('plik.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            tp = type(row[int(colnum)])
            print(tp)


showcolumn()
datatype()

