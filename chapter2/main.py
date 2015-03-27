# coding: utf-8
from __future__ import division, print_function, unicode_literals
import sys
import re
from operator import itemgetter
import codecs
import random
import collections
import itertools

def set_encoding(enc='utf_8'):
    sys.stdin = codecs.getreader(enc)(sys.stdin)
    sys.stdout = codecs.getwriter(enc)(sys.stdout)
    sys.stderr = codecs.getwriter(enc)(sys.stderr)

FILENAME = './hightemp.txt'

def read_eachline(fname):
    with codecs.open(fname, 'r', 'utf_8') as f:
        for line in f:
            yield line.strip()

def proc10():
    line_num = 0
    for line in read_eachline(FILENAME):
        line_num += 1
    print('# of line: ' + str(line_num))

def proc11():
    for line in read_eachline(FILENAME):
        print(re.sub(r'\t', ' ', line))

def proc12():
    with codecs.open('col1.txt', 'w', 'utf_8') as col1:
        with codecs.open('col2.txt', 'w', 'utf_8') as col2:
            for line in read_eachline(FILENAME):
                sp = line.split('\t')
                print(sp[0], file=col1)
                print(sp[1], file=col2)

def proc13():
    for x, y in zip(read_eachline('col1.txt'), read_eachline('col2.txt')):
        print('{}\t{}'.format(x.strip(), y.strip()))

def read_n():
    return int(raw_input('n> '))

def proc14():
    n = read_n()
    for line in read_eachline(FILENAME):
        if n <= 0:
            break
        print(line)
        n -= 1

def proc15():
    n = read_n()
    # see also: http://docs.python.jp/2/library/collections.html#id1
    print('\n'.join(collections.deque(read_eachline(FILENAME), n)))

def proc16():
    n = read_n()
    c = 0
    f = None
    for line in read_eachline(FILENAME):
        if c % n == 0:
            if f:
                f.close()
            f = codecs.open('split{}.txt'.format(c // n), 'w', 'utf_8')
        print(line, file=f)
        c += 1
    if f:
        f.close()

def proc17():
    s = set(itertools.imap(lambda line: line.split('\t')[0], read_eachline(FILENAME)))
    for w in s:
        print(w)

def proc18():
    d = map(lambda line: line.split('\t'), read_eachline(FILENAME))
    d.sort(key=itemgetter(2), reverse=True)
    for datum in d:
        print('\t'.join(datum))

def proc19():
    c = collections.Counter(itertools.imap(lambda line: line.split()[0], read_eachline(FILENAME)))
    l = list(c.iteritems())
    l.sort(key=itemgetter(1), reverse=True)
    for item in l:
        print(item[1], item[0])

def main():
    if len(sys.argv) < 2:
        print('usage: python {} NUM'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    num = int(sys.argv[1])
    eval('proc{}()'.format(num))

if __name__ == '__main__':
    set_encoding()
    main()
