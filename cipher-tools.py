import sys
import json
import math

CIPHERS = ['-ca', '-rf']
CHOICE = ['-e', '-d']


def get_args():
    # correct number of args
    if len(sys.argv) == 5:
        # parse args
        args = sys.argv[1:]
        if args[0] in CIPHERS:
            if args[1] in CHOICE:
                if args[3].isnumeric():
                    args[3], args[2] = int(args[3]), args[2].lower()
                    return args
                else:
                    print('invalid arguments: python3 cipher.py %s %s %s [%s]' % (args[0], args[1], args[2], args[3]))
            else:
                print('invalid arguments: python3 cipher.py %s [%s] %s %s' % (args[0], args[1], args[2], args[3]))
        else:
            print('invalid arguments: python3 cipher.py [%s] %s %s %s' % (args[0], args[1], args[2], args[3]))
    # cracking args
    elif len(sys.argv) == 3 or len(sys.argv) == 4 and sys.argv[1] == '-c':
        return sys.argv[1:]
    # check if --help
    elif len(sys.argv) == 2 and sys.argv[1] == '--help':
        print(
            'Usage:\n\t(use - as space in text)\n\ncipher cracking:\n\t\tpython3 cipher-tools.py -c [ciphertext] [accuracy]\t(crack ciphertext with accuracy number of matches)\n\tor\n\t\tpython3 cipher-tools.py -c [ciphertext]\t\t\t(crack with default accuracy of 5)\n\nrailfence cipher:\n\t\tpython3 cipher-tools.py -rf -e [plaintext] [rails]\t(to encrypt)\n\tor\n\t\tpython3 cipher-tools.py -rf -d [ciphertext] [rails]\t(to decrypt)\n\ncaesar cipher:\n\t\tpython3 cipher-tools.py -ca -e [plaintext] [shift]\t(to encrypt)\n\tor\n\t\tpython3 cipher-tools.py -ca -d [ciphertext] [shift]\t(to decrypt)\n\n')
    # anything else
    else:
        print('invalid arguments, use --help')
    exit()


def railfence_encrypt(plain_text, rails):
    output, fm_text = '', ''
    # remove any -'s
    for c in plain_text:
        if c != '-':
            fm_text += c

    grid = [['-'] * len(fm_text) for i in range(rails)]

    # shifting output -> grid
    x, y, count, finished = 0, 0, 0, False

    while not finished:
        while x < rails and count < len(fm_text):
            grid[x][y], y, x, count = fm_text[count], y + 1, x + 1, count + 1
        x = x - 2
        while x > -1 and count < len(fm_text):
            grid[x][y], y, x, count = fm_text[count], y+1, x-1, count + 1
        x = 1
        if count == len(fm_text):
            finished = True

    # formatting grid -> output
    for row in grid:
        for char in row:
            if char != '-':
                output += char
    return output


def railfence_decrypt(cipher_text, rails):
    output = ''
    grid = [['-'] * len(cipher_text) for i in range(rails)]
    temp = ''

    for c in cipher_text:
        if c != '-':
            temp += c

    cipher_text = temp

    x, y, count, empty_count, finished = 0, 0, 0, 0, False

    # set all diagonal spaces = &
    while not finished:
        while x < rails and empty_count < len(cipher_text):
            grid[x][y], y, x, empty_count = '&', y + 1, x + 1, empty_count + 1
        x = x - 2
        while x > -1 and empty_count < len(cipher_text):
            grid[x][y], y, x, empty_count = '&', y+1, x-1, empty_count + 1
        x = 1
        if empty_count == len(cipher_text):
            finished = True

    for i in range(0, rails):
        for j in range(0, len(cipher_text)):
            if grid[i][j] == '&':
                grid[i][j], count = cipher_text[count], count + 1

    # have grid with cipher filled

    # grid -> output
    x, y, finished = 0, 0, False

    while not finished:
        while x < rails and len(output) != len(cipher_text):
            output, y, x = output + grid[x][y], y + 1, x + 1
        x = x - 2
        while x > -1 and len(output) != len(cipher_text):
            output, y, x = output + grid[x][y], y+1, x-1
        x = 1
        if len(output) == len(cipher_text):
            finished = True

    return output


def caesar_encrypt(plain_text, shift):
    output = ''
    for c in plain_text:
        output += c if c == '-' else chr(int(((ord(c) - 97) - shift) % 26) + 97)
    return output


def caesar_decrypt(cipher_text, shift):
    output = ''
    for c in cipher_text:
        output += c if c == '-' else chr(int(((ord(c) - 97) + shift) % 26) + 97)
    return output


def brute_crack(cipher_text, accuracy):
    words = json.loads(open('words.json').read())
    possible_plaintext = []

    # ceasar brute
    for step in range(1, 27):
        output = caesar_decrypt(cipher_text, step)
        tally = 0
        for word in words:
            if word in output:
                tally += 1
        if tally >= accuracy:
            possible_plaintext.append('#%d CAESAR: \"%s\" with step %d' % (len(possible_plaintext) + 1, output, step))

    # railfence brute
    for rail in range(3, math.floor(len(cipher_text) / 2)):
        output = railfence_decrypt(cipher_text, rail)
        tally = 0
        for word in words:
            if word in output:
                tally += 1
        if tally >= accuracy + 1:
            possible_plaintext.append('#%d RAILFENCE: \"%s\" with rail number %d' % (len(possible_plaintext) + 1, output, rail))

    return possible_plaintext


args = get_args()

if args[0] == '-ca':
    if args[1] == '-e':
        print(caesar_encrypt(args[2], args[3]))
    else:
        print(caesar_decrypt(args[2], args[3]))
elif args[0] == '-rf':
    if args[1] == '-e':
        print(railfence_encrypt(args[2], args[3]))
    else:
        print(railfence_decrypt(args[2], args[3]))
elif args[0] == '-c':
    if len(args) == 2:  # if no accuracy given, use 5
        pos = brute_crack(args[1], 5)
    else:
        pos = brute_crack(args[1], int(args[2]))
    if len(pos) == 0:
        print('no matches found\ntry a lower accuracy')
    else:
        print('POSSIBLE SOLUTIONS')
        for solution in pos:
            print(solution)
