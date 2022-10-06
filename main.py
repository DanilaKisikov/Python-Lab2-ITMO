import csv

red = '\u001b[41m'
Blue = '\u001b[44m'
white = '\u001b[47m'
yellow = '\u001b[43m'
green = '\u001b[42m'
nothing = '\u001b[0m'

# Флаг

for i in range(9):
    if i<=2:
        print(yellow + '  '* 30 + nothing)
    elif i <= 5:
        print(green + '  ' * 30 + nothing)
    else:
        print(red + '  ' * 30 + nothing)

# Узор
print()
for i in range(3):
    for k in range(8):
        print(' ' * (100-(k**2) - 2*(k+2)) + red + ' ' * (2*k + 1) + nothing + '  '*(k**2) + red + ' ' * (2*k + 1) + nothing + '     ')
    print()

# График

array = [['   ' for col in range(22)] for row in range(12)]
yes = []
xes = []

for x in range(-10,12):
    y = abs(x)
    yes.append(y)
    xes.append(x)
print('\n' + str(yes) + '\n' + str(xes) + '\n')


for i in range(22):
    if len(str(i - 10)) == 2:
        array[-1][i] = Blue + ' ' + str(i - 10) + nothing
    elif len(str(i - 10)) == 3:
        array[-1][i] = Blue + str(i - 10) + nothing
    else:
        array[-1][i] = Blue + '  ' + str(i - 10) + nothing

for i in range(11):
    if len(str(11 - i)) == 2:
        array[i][10] = Blue + ' ' + str(11 - i) + nothing
    else:
        array[i][10] = Blue + '  ' + str(11 - i) + nothing

for x1 in range(len(xes)):
    if len(str(yes[x1])) == 2:
        array[11 - yes[x1]][10 + xes[x1]] = red + ' ' + str(yes[x1]) + nothing
    else:
        array[11 - yes[x1]][10 + xes[x1]] = red + '  ' + str(yes[x1]) + nothing

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end= ' ')
    print()
print('\n\n')

# Диаграмма
for12y = 0
all = 0

with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        try:
            if int(row[5]) <= 12:
                for12y += 1
        except:
            yuyuy = 0
        all += 1

percent = for12y / all
percentAn = 1 - percent

diagramm = [['    ' for j in range(20)] for i in range(11)]

for i in range(len(diagramm)):
    if len(str((10-i)*10)) == 3:
        diagramm[i][0] = Blue + str((10-i)*10) + '%' + nothing
    elif len(str((10-i)*10)) == 2:
        diagramm[i][0] = Blue + str((10 - i) * 10) + '% '+ nothing
    else:
        diagramm[i][0] = Blue + str((10 - i) * 10) + '%  ' + nothing

    if percent >= (10 - i) / 10:
        diagramm[i][2] = red + '    ' + nothing
    if percentAn >= (10 - i) / 10:
        diagramm[i][4] = red + '    ' + nothing

for i in range(len(diagramm)):
    for j in range(len(diagramm[i])):
        print(diagramm[i][j], end=' ')
    print()
print(Blue + '       Для 12 лет  Другие' + nothing)

print('\n' + '\n' + str(percent))
print(percentAn)
print(all)
print(for12y)