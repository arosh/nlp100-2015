# coding: utf-8
from __future__ import division, print_function, unicode_literals
from collections import namedtuple
import sys
import codecs
import MeCab
import subprocess
import os
import itertools


def set_encoding(enc='utf_8'):
    sys.stdin = codecs.getreader(enc)(sys.stdin)
    sys.stdout = codecs.getwriter(enc)(sys.stdout)
    sys.stderr = codecs.getwriter(enc)(sys.stderr)


FILENAME = './neko.txt'
DICTDIR = '/Users/arosh/opt/neologd'


def normalize(s):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'normalize_neologd.rb')
    p = subprocess.Popen(
        'ruby {}'.format(path),
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out, err = p.communicate(s.encode('utf_8'))
    if p.poll():
        p.terminate()
    out = out.decode('utf_8').strip()
    err = err.decode('utf_8').strip()
    if err:
        print('[normalize_neologd] {}'.format(err), file=sys.stderr)
    return out


def tagging():
    with codecs.open(FILENAME, encoding='utf_8') as f:
        s = normalize(f.read()).encode('utf_8')
    MeCabNode = namedtuple('MeCabNode', ['surface', 'base', 'pos', 'pos1'])
    opt = '-d {}'.format(DICTDIR).encode('utf_8')
    tagger = MeCab.Tagger(opt)
    node = tagger.parseToNode(s)
    while node:
        surface = node.surface.decode('utf_8')
        if len(surface) > 0:
            sp = node.feature.decode('utf_8').split(',')
            base = sp[6]
            pos = sp[0]
            pos1 = sp[1]
            yield MeCabNode(surface, base, pos, pos1)
        node = node.next


def proc31():
    verbs = itertools.ifilter(lambda m: m.pos == '動詞', tagging())
    surfaces = itertools.imap(lambda m: m.surface, verbs)
    for s in surfaces:
        print(s)


def proc32():
    verbs = itertools.ifilter(lambda m: m.pos == '動詞', tagging())
    bases = itertools.imap(lambda m: m.base, verbs)
    for s in bases:
        print(s)

def proc33():
    verbs = itertools.ifilter(lambda m: m.pos == '名詞' and m.pos1 == 'サ変接続', tagging())
    for v in verbs:
        print(v.surface)

def main():
    if len(sys.argv) < 2:
        print('usage: python {} NUM'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    num = int(sys.argv[1])
    eval('proc{}()'.format(num))


if __name__ == '__main__':
    set_encoding()
    main()
