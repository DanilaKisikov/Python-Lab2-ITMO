import time
import os

Red = '\u001b[45m'
Yellow = '\u001b[40m'
Nothing = '\u001b[0m'

i = 0
a = 0

running = True

while running:
    print(((Red + ' ' * i + Nothing) * 6 + (Yellow + ' ' * (10-i) + Nothing) * 6 + Nothing + '\n') * 6)

    if a == 0:
        #print((Red + '   ' * i + Nothing + '\n') * 6 + Nothing + '\n' * 13)
        i += 1
        if i == 10:
            a = 1

    elif a == 1:
        #print((Yellow + '   ' * (10-i) + Nothing + '\n') * 6 + Nothing + '\n' * 13)
        i -= 1
        if i == 0:
            a = 0

    time.sleep(0.1)
    #print('\n' * 10)
    os.system('clear')

