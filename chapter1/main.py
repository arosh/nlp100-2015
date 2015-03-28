# coding: utf-8
from __future__ import division, print_function, unicode_literals
import sys
import re
from operator import itemgetter
import codecs
import random


def set_encoding(enc='utf_8'):
    sys.stdin = codecs.getreader(enc)(sys.stdin)
    sys.stdout = codecs.getwriter(enc)(sys.stdout)
    sys.stderr = codecs.getwriter(enc)(sys.stderr)


def proc0():
    s = 'stressed'
    t = s[::-1]
    print('t = ' + t)


def proc1():
    s = 'パタトクカシーー'
    t = s[1::2]
    print('t = ' + t)


def proc2():
    s = 'パトカー'
    t = 'タクシー'
    u = ''.join(s[i] + t[i] for i in xrange(len(s)))
    print('u = ' + u)


def proc3():
    s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    ss = s.split(' ')
    t = [len(re.sub('\W', '', w)) for w in ss]
    print('repr(t) = ' + repr(t))


def proc4():
    s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    a = map(lambda x: x - 1, [1, 5, 6, 7, 8, 9, 15, 16, 19])
    m = {}
    for i, ss in enumerate(s.split(' ')):
        if i in a:
            m[ss[:1]] = i + 1
        else:
            m[ss[:2]] = i + 1
    l = [item for item in m.iteritems()]
    l.sort(key=itemgetter(1))
    print(repr(l))


def proc5():
    s = raw_input('> ')
    n = 2
    print('# word {}-gram #'.format(n))
    print(repr(word_n_gram(s, 2)))
    print('# char {}-gram #'.format(n))
    print(repr(char_n_gram(s, 2)))


def char_n_gram(s, n):
    return [s[i:i + n] for i in xrange(len(s) - n + 1)]


def word_n_gram(s, n, delim=' '):
    ws = s.split(delim)
    return [ws[i:i + n] for i in xrange(len(ws) - n + 1)]


def proc6():
    s = 'paraparaparadise'
    t = 'paragraph'
    X = set(char_n_gram(s, 2))
    Y = set(char_n_gram(t, 2))
    print('X & Y = ' + repr(X & Y))
    print('X | Y = ' + repr(X | Y))
    print('X - Y = ' + repr(X - Y))
    print('"se" in X = ' + repr(u"se" in X))
    print('"se" in Y = ' + repr(u"se" in Y))


def proc7():
    def fn(x, y, z):
        return '{}時の{}は{}'.format(x, y, z)

    print(fn(12, '気温', 22.4))


def proc8():
    text = raw_input('> ')

    def cipher(s):
        def repl(c):
            if re.match(r'\w', c):
                return chr(219 - ord(c))
            return c

        return ''.join(repl(c) for c in s)

    print(cipher(text))


def proc9():
    text = raw_input('> ')

    def typoglycemia(s):
        ret = []
        for ss in s.split(' '):
            if len(ss) < 4:
                ret.append(ss)
                continue
            t = list(ss)[1:-1]
            random.shuffle(t)
            ret.append(ss[0] + ''.join(t) + ss[-1])
        return ' '.join(ret)

    print(typoglycemia(text))


def main():
    if len(sys.argv) < 2:
        print('usage: python {} NUM'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    num = int(sys.argv[1])
    eval('proc{}()'.format(num))


if __name__ == '__main__':
    set_encoding()
    main()
