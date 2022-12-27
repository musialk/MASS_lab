#https://www.kaggle.com/impapan/student-performance-data-set
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("student-mat.csv", sep=';')

#Ile kobiet lub mężczyzn studiuje matematyke?
sex = students.groupby('sex').size()
print(sex)
#Na kierunku matematyka jest więcej kobiet, niż mężczyzn.

#Ile kobiet lub mężczyzn chce kontynuować naukę?
students['higher_sex'] = students['higher'] + students['sex']
higher = students.groupby('higher_sex').size()
print(higher)
#Tylko 4 kobiety nie chcą kontynuować nauki, natomiast pomimo, że mężczyzn jest mniej w ogóle na kierunku matematycznym
#to aż 16 nie chce kontynuować nauki.

#Jaka jest zależność od czasu drogi dojazdu do miejsca nauki a czasem nauki?
studytime = students.groupby('studytime').size()
traveltime = students.groupby('traveltime').size()

times = pd.Series(studytime, name="Study time")
timet = pd.Series(traveltime, name="Travel time")

fig, wykres=plt.subplots()
wykres.plot(times, label="Study time")
wykres.plot(timet, label="Travel time")
wykres.legend()
fig.suptitle('Wykres zależności czasu dojazdu do szkoły od czasu nauki')
plt.show()
#Po analizie za pomocą wykresów można stwierdzić, że najwięcej się uczą uczniowie, którzy mają średni czas powrotu do
#domu, a najmniej osoby, które mają bardzo długi czas powrotu do domum

#Czy jest więcej studentów z miasta czy ze wsi?
adres = students.groupby('address').size()
adres.plot.bar()
plt.show()
#Więcej osób jest z miasta.

#Czy osoby z problemami zdrowotnymi odwiedzały pielęgniarke?
df = pd.DataFrame(np.random.rand(200,1), columns=['przyjaciele'])
df['zdrowie'] = pd.Series(students['health'])
df['friends']  = pd.Series(students['goout'])
plt.figure()
bp = df.boxplot(column=['przyjaciele'], by=['zdrowie','friends'], figsize=[20,10])
plt.show()
#Można zauważyć, że skrajne wartości jak np. 1=bardzo zły stan zdrowia oraz 1=brak spotkań ze znajomymi stanowią bardzo
#niewielkie grupy, jak również wartości z drugiej skrajności. Natomiast największą grupę stanowią osoby wartościami 3,
#czyli osoby z raczej dobrym stanem zdrowia spotykające się czasami ze znajomymi.

#Ile kobiet a ile mężczyzn ma romantyczne relacje podczas studiów?
students['couple'] = students['romantic'] + students['sex']
couple = students.groupby('couple').size()
print(couple)
labels = 'noF','noM','yesF','yesM'

fig2, ax1 = plt.subplots()
ax1.pie(couple, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')
plt.show()
#Z wykresu wynika, że więcej 20% kobiet jest w związku i niewiele mniej mężczyzn, jednak ponad połowa studentów pozostaje
#singlami.
