# improve limit argument
# improve size argument

# improve methods' return
#     do not use dozens of variables but organize a list

# check_only_except is probably duplicating the variables
#     set(m) resolves but is unnecessary processing

# improve check_only_except (make just 1 loop)
# create [--for-all-only v1, v2, ...] [--for-all-except v1, v2, ...]
#     just for mother father and property
#     and improve the operation of --only/except

# is 'options' variable necessary?

import sys        # argv, exit
import random     # choice, sample
import itertools  # permutations, combinations

m = []
only = []
except_ = []

size = 0
x, v = 0, 0
min, max = 8, 8

familly = ['Target\'s']
vowels = ['a', 'e', 'i', 'o', 'u']

# create argument_v to all variables

argument_b = {'d': [0, 1], 'n': [1, 3], 'n2': [3, 5], 'n3': [5, 9],
            'n4': [9, 12], 'n5': [12, 15], 'n6': [15, 17], 'n7': [17, 19],
            'v': [19, 21], 'v2': [29, 31], 'c': [21, 23], 'c2': [31, 33],
            'ln': [23, 26], 'lsn': [26, 29]}
argument_tb = {'D': [0, 1], 'N': [1, 19], 'L': [23, 29]}
        #    'v': [19, 21], 'v2': [29, 31], 'c': [21, 23], 'c2': [31, 33],
        # to do..

translate_v = {97: '4', 101: '3', 105: '1', 111: '0'}
translate_c = {98: '8', 116: '7', 122: '2', 103: '6', 115: '5'}

options = ['-h', '--help', '-s', '--size', '-v', '--variables',
        '-m', '--mother', '-f', '--father', '-p', '--pet',
        '-l', '--lenght', '-lim', '--limit', '--only', '--except']

exemples = ['Napoleon Bonaparte 15 08 1769', 'Elizaberti II 21 04 1926',
        'Jesus Christ 00 00 9867', 'Stan Lee 28 12 1922', 'Grazzy Garcia 17 08 2000',
        ]

def banner():
    b = '''
    \033[1;37m
     ____                    _
    |  _ \    ___    _ __   (_)
    | |_) |  / _ \  | '_ \  | |
    |  __/  | (_) | | |_) | | |         (Popis)
    |_|      \___/  | .__/  |_|
                    |_|         \033[05mv.1.0\033[25m
    Permutation Of Personal information (Software)
    \033[1;37m
    [*] If you don't know day month or year put 00 in place
    [*] If you dom't know surname put the same as name '''
    print(b)

def help():
    h = '''
    usage: popi [-h] [-s] [-v] [-m] [-f] [-p] [-l min max]
                [-lim x] [--only v1, v2, ...] [--except v1, v2, ...]

    optional arguments:
        -h, --help             show this help message and exit
        -s, --size             print how many words will be created and exit
        -v, --variables        print all mapped variables
        -m, --mother           allow popi use mother's information
        -f, --father           allow popi use father's information
        -p, --pet              allow popi use pet's information
        -l, --lenght min max   set min and max lenght to the passwords
        -lim, --limit x        limits wordlist to a maximum of x words
        --only v1, v2, ...     allow popi use only variables/(top)blocks v1, v2, ...
        --except v1, v2, ...   allow popi use all variables/(top)blocks except v1, v2, ...

    variables/blocks/topblocks:

        D_y                         ( d   )   [ D ]

        n_n, N_n                    ( n   )
        s_n, S_n                    ( n2  )
        ns_n, Ns_n, nS_n, NS_n      ( n3  )
        nn_n, Nn_n, NN_n            ( n4  )   [ N ]
        nnn_n, Nnn_n, NNN_n         ( n5  )
        Name, NAME                  ( n6  )
        S_name, S_NAME              ( n7  )

        V_n, V_sn                   ( v   )
        Vd_n, Vd_sn                 ( v2  )   [ V ]

        C_n, C_sn                   ( c   )
        Cd_n, Cd_sn                 ( c2  )   [ C ]

        leet_vn, Leet_vn, LEET_vn   ( ln  )
        leet_an, Leet_an, LEET_an   ( lsn )   [ L ]

    by default target is mapped with all variables       { + name
               mother and father only mapped by n, n2, d { surname
               pet only mapped by n, d                   { d/m/y
    '''
    print(h)

def check_date(day, month, year):
    if not int(day):
        day = ''
    if not int(month):
        month = ''
    if not int(year):
        year = ''
    return day, month, year

def check_only_except(argument, m, meth):
    try:
        for i in argument:
            me = meth[argument_b[i][0]:argument_b[i][1]]
            for j in me:
                if type(j) is list:
                    yield j
                else:
                    yield me
    except:
        for i in argument:
            me = meth[argument_tb[i][0]:argument_tb[i][1]]
            for j in me:
                if type(j) is list:
                    yield j
                else:
                    yield me

def entry(pet, i):
    if pet:
        e = input('\n[*] Enter: pet\'s name day month year\n[+] ').split()
        if len(e)!=4:
            print('\n[!!] Enter 4 values')
            e = entry(1, 'pet\'s')
        if not e[0].isalpha():
            print('\n[!!] Name is incorrect')
            e = entry(1, 'pet\'s')
        if not (e[1]+e[2]+e[3]).isnumeric():
            print('\n[!!] Day month or year is incorrect')
            e = entry(1, 'pet\'s')
        return e

    e = input('\n[*] Enter: %s name surname day month year:\n[*] e.g. %s\n[+] ' %(i, random.choice(exemples))).split()
    if len(e)!=5:
        print('\n[!!] Enter 5 values')
        e = entry(0, i)
    if not (e[0]+e[1]).isalpha():
        print('\n[!!] Name or surname is incorrect')
        e = entry(0, i)
    if not (e[2]+e[3]+e[4]).isnumeric():
        print('\n[!!] Day month or year is incorrect')
        e = entry(0, i)
    return e

def methods(name, s_name, year):

    D_y = year[2:]

    Name = name.capitalize()
    NAME = name.upper()
    S_name = s_name.capitalize()
    S_NAME = s_name.upper()

    n_n = name[0]
    N_n = name[0].upper()

    s_n = s_name[0]
    S_n = s_name[0].upper()

    nn_n = name[:2]
    Nn_n = name[:2].capitalize()
    NN_n = name[:2].upper()

    nnn_n = name[:3]
    Nnn_n = name[:3].capitalize()
    NNN_n = name[:3].upper()

    ns_n = name[0].lower() + s_name[0].lower()
    Ns_n = name[0].upper() + s_name[0].lower()
    nS_n = name[0].lower() + s_name[0].upper()
    NS_n = name[0].upper() + s_name[0].upper()

    leet_vn = name.lower().translate(translate_v)
    Leet_vn = name.lower().translate(translate_v).capitalize()
    LEET_vn = name.lower().translate(translate_v).upper()
    leet_an = s_name.lower().translate(translate_c).translate(translate_v)
    Leet_an = s_name.lower().translate(translate_c).translate(translate_v).capitalize()
    LEET_an = s_name.lower().translate(translate_c).translate(translate_c).upper()

    V_n = ''.join(i for i in name if i in vowels)
    V_sn = ''.join(i for i in s_name if i in vowels)

    C_n = ''.join(i for i in name if i not in vowels)
    C_sn = ''.join(i for i in s_name if i not in vowels)

    Vd_n = [name[i]*2 for i in range(len(name)-1) if name[i]==name[i+1] and name[i] in vowels]
    Vd_sn = [s_name[i]*2 for i in range(len(s_name)-1) if s_name[i]==s_name[i+1] and s_name in vowels]

    Cd_n = [name[i]*2 for i in range(len(name)-1) if name[i]==name[i+1] and name[i] not in vowels]
    Cd_sn = [s_name[i]*2 for i in range(len(s_name)-1) if s_name[i]==s_name[i+1] and s_name not in vowels]

    #      0    1    2    3    4    5     6     7     8     9     10    11     12     13    14     15    16     17      18     19   20    21    22    23       24       25       26       27       28      29    30     31    32
    return D_y, n_n, N_n, s_n, S_n, ns_n, Ns_n, nS_n, NS_n, nn_n, Nn_n, NN_n, nnn_n, Nnn_n, NNN_n, Name, NAME, S_name, S_NAME, V_n, V_sn, C_n, C_sn, leet_vn, Leet_vn, LEET_vn, leet_an, Leet_an, LEET_an, Vd_n, Vd_sn, Cd_n, Cd_sn

def main():

    global m
    global size
    global x, v
    global only
    global except_
    global familly
    global min, max

    banner()

    args = sys.argv


    if any(i in ('-h', '--help') for i in args):
        help()
        sys.exit()

    if any(i in ('-s', '--size') for i in args):
        size = 1

    if any(i in ('-v', '--variables') for i in args):
        v = 1

    if any(i in ('-l', '--lenght') for i in args):
        try:
            indx = args.index('-l')
        except:
            indx = args.index('--lenght')
        try:
            min, max = int(args[indx+1]), int(args[indx+2])
        except IndexError:
            print('\n[!!] You have to pass 2 numbers for lenght argument')
            sys.exit()
        args.remove(str(min))
        args.remove(str(max))

    if any(i in ('-lim', '--limit') for i in args):
        try:
            x = args.index('-lim')
        except:
            x = args.index('--limit')
        try:
            x = int(args[x+1])
        except IndexError:
            print('\n[!!] You have to pass a number for limit argument')
            sys.exit()
        args.remove(str(x))

        print(check)
    if any(i in ('-m', '--mother') for i in args):
        familly.append('Mother\'s')

    if any(i in ('-f', '--father') for i in args):
        familly.append('Father\'s')

    if any(i in ('-p', '--pet') for i in args):
        familly.append('Pet\'s')

    if '--only' in args:
        try:
            only = args[args.index('--only')+1:]
        except IndexError:
            print('\n[!!] You have to pass variables for only argument')
        only = [i for i in only if i not in options]
        args = [i for i in args if i not in only]
        print(only)

    if '--except' in args:
        try:
            except_ = args[args.index('--except')+1:]
        except IndexError:
            print('\n[!!] You have to pass variables for except argument')
        except_ = [i for i in except_ if i not in options]
        args = [i for i in args if i not in except_]
        print(except_)

    for i in args[1:]:
        if i not in options:
            print('[!!] Argument not recognized: ' + i)
            sys.exit()


    for i in familly:
        if i=='Pet\'s':
            name, day, month, year = entry(1, i)
        else:
            name, s_name, day, month, year = entry(0, i)
        day, month, year = check_date(day, month, year)

        meth = methods(name, s_name, year)
        if i=='Target\'s':
            if not only and not except_:
                m.extend(i for i in [name, s_name, day, month, year])
                m.extend(i for i in meth[:-4])
                m.extend(i for j in meth[-4:] for i in j)
            elif only:
                only = check_only_except(only, m, meth)
                m.extend(i for j in only for i in j)
            elif except_:
                except_ = check_only_except(except_, m, meth)
                m.extend(i for j in meth if j not in except_ for i in j)
        elif i=='Pet\'s':
            m.extend(i for i in [name, day, month, year])
            m.extend(meth[0], meth[5], meth[6]) # D_y n_n N_n
        else:
            m.extend(i for i in [name, s_name, day, month, year])
            m.extend(meth[0], meth[5], meth[6], meth[7], meth[8]) # D_y n_n N_n s_n S_n


    m = set(m)
    if v:
        for i in m:
            print(i)

    print('\n[*] Generating wordlist\033[05m...\033[25m')

    # combines all variables that are the desired size (8 default)
    cList = (c for length in range(1, max+1) for c in itertools.combinations(m, length) if len(''.join(c))>=min and len(''.join(c))<=max)

    pList = [''.join(p) for i in cList for p in itertools.permutations(i)]
    pList = set(pList)

    # shuffle and limits the list
    if not x:
        x = len(pList)
    if x<=len(pList):
        pList = random.sample(pList, x)
    else:
        pList = random.sample(pList, len(pList))


    # write output to file if -s argument were not passed
    if not size:
        output = open('output.txt', 'w')
    for i in pList:
        if not size:
            output.write(i + '\n')
    if not size:
        output.close()

    print('\n[*] The wordlist has ' + str(len(pList)) + ' words')


try:
     main()
except BaseException as e:
    print(e)
