import re
import easygui

file = easygui.fileopenbox()

raw = open(file, 'r')
ready = open('combo.txt', 'w')


for line in raw:
    pieces = line.split(":")
    email = pieces[0]
    password = pieces[1]
    count = count + 1
    pasw = re.findall(r"[A-Za-z0-9\.\-+_]+[A-Za-z0-9\.\-+_]+", str(password))
    combo = (str(email)+':'+str(pasw[0]))
    ready.writelines(combo+'\n')

print('ready')

#written by noopartz
