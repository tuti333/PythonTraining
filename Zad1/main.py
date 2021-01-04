import webbrowser
import re

print("Program sprawdza czy podany tekst jest palindromem")
#Get data from user
str = input("Podaj sprawdzany tekst:").lower()
#Remove chars other than alphanumerical
str = re.sub('[^0-9a-zA-Z]+', '', str)
#Get reversed string
rev_str = str[::-1]
print(rev_str);
if str == rev_str:
    print("Podany tekst jest palindromem")
else:
    print("Podany tekst nie jest palindromem")

if input("Wpisz y by wyswietlic przykladowe slowa ulozone z liter ze slowa " + str + "\n") == "y":
    webbrowser.open('https://poocoo.pl/scrabble-slowa-z-liter/' + str)
