import os.path
import sys

def read_file(filename):
    locale = dict()
    charmap = dict()
    locales = []
    charmaps = []
    if not os.path.exists(filename):
        print('error: no such file')
        exit(0)
    with open(filename) as file:
        for line in file:
            line = line.strip().split(',')
            if line[0] == 'locale':
                if line[1] not in locale:
                    locale[line[1]] = []
                locale[line[1]].append(line[2])
                locales.append(line[2])
            elif line[0] == 'charmap':
                if line[1] not in charmap:
                    charmap[line[1]] = []
                charmap[line[1]].append(line[2])
                charmaps.append(line[2])
    return locale, locales, charmap, charmaps
opt = sys.argv[1]

if opt == '-a':
    if len(sys.argv) < 3:
        print('it misses the argument file')
        exit(0)
    _,locales,_,_ = read_file(sys.argv[2])
    if len(locales) != 0:
        print('Available locales:')
        for l in locales:
            print(l)
    else:
        print('No locales available')
elif opt == '-m':
    if len(sys.argv) < 3:
        print('it misses the argument file')
        exit(0)
    _,_,_,charmaps = read_file(sys.argv[2])
    if len(charmaps) != 0:
        print('Available charmaps:')
        for c in charmaps:
            print(c)
    else:
        print('No charmaps available')
elif opt == '-l':
    if len(sys.argv) < 4:
        print('it misses the language argument or argument file')
        exit(0)
    language = sys.argv[2]
    locale,_,charmap,_ = read_file(sys.argv[3])
    lnum = len(locale[language]) if language in locale else 0
    cnum = len(charmap[language]) if language in charmap else 0
    if lnum == 0 and cnum == 0:
        print('No locales or charmaps in this language')
    else:
        print(f'Language {language}:')
        print(f'Total number of locales: {lnum}' )
        print(f'Total number of charmaps: {cnum}' )
elif opt == '-v':
    name = 'name'
    surname = 'surname'
    studentID = 12345
    date = '2024/4/22'
    print(f'{name}, {surname}, {studentID}, {date}')
else:
    print("this option doesn't exist")

