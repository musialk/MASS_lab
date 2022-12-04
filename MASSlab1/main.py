import datetime

import pandas as pd

#zad1. Łączną liczbę filmów (Movie) i liczba programów telewizyjnych (TV Show).
netflix = pd.read_csv("netflix_titles.csv", sep=",")
liczba = netflix.groupby('type').size()
print(liczba)

#zad2. Liczbę filmów (Movie) i liczba programów telewizyjnych (TV Show) dodanych (date_added) w każdym roku.
netflix[['miesiac','rok']] = netflix['date_added'].str.split(',',expand=True)
netflix['film_rok'] = netflix['type'] + ',' + netflix['rok']
filmrok = netflix.groupby('film_rok').size()
print(filmrok)

#zad3. Liczbę filmów (Movie) i liczbę programów telewizyjnych (TV Show) dodanych w każdej kategorii (listed_in)
netflix['film_kategoria'] = netflix['type'] + ',' + netflix['listed_in']
filmkategoria = netflix.groupby('film_kategoria').size()
print(filmkategoria)

#zad4. Liczbę filmów (Movie) i liczbę programów telewizyjnych (TV Show) według kraju (country).
netflix['film_kraj'] = netflix['type'] + ',' + netflix['country']
filmkraj = netflix.groupby('film_kraj').size()
print(filmkraj)

#zad5. Średni czas od momentu premiery (release_year) do dodania w każdym roku
netflix['rok'] = pd.to_datetime(netflix['rok'], format=' %Y')
netflix['release_year'] = pd.to_datetime(netflix['release_year'], format='%Y')
netflix['odejmowanie'] = netflix['rok'] - netflix['release_year']
print(netflix['odejmowanie'].mean())