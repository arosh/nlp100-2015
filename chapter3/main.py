# coding: utf-8
from __future__ import division, print_function, unicode_literals
import sys
import re
import codecs
import json
import gzip


def set_encoding(enc='utf_8'):
    sys.stdin = codecs.getreader(enc)(sys.stdin)
    sys.stdout = codecs.getwriter(enc)(sys.stdout)
    sys.stderr = codecs.getwriter(enc)(sys.stderr)


FILENAME = './jawiki-country.json.gz'


def get_text_about_uk():
    reader = codecs.getreader('utf_8')
    with gzip.open(FILENAME) as f:
        for line in reader(f):
            o = json.loads(line)
            if o['title'] == 'イギリス':
                return o['text']


def proc20():
    print(get_text_about_uk())


def proc21():
    for line in get_text_about_uk().splitlines():
        if re.match(r'\[\[Category:(.+?)\]\]', line):
            print(line)


def proc22():
    for line in get_text_about_uk().splitlines():
        m = re.match(r'\[\[Category:(.+?)(\|.+?)?\]\]', line)
        if m:
            print(m.group(1))


def proc23():
    for line in get_text_about_uk().splitlines():
        m = re.match(r'(={2,})\s*(.+?)\s*(={2,})', line)
        if m:
            print(len(m.group(1)) - 1, m.group(2))


def proc24():
    it = re.finditer(r'\[\[(ファイル|File):(.+?)\|', get_text_about_uk())
    for m in it:
        print(m.group(2))


def proc25():
    d = {}
    for line in get_text_about_uk().splitlines():
        m = re.match(r'\|(.+?) = (.+)', line)
        if m:
            d[m.group(1)] = m.group(2)
    return d


def proc26():
    d = {}
    for k, v in proc25().iteritems():
        s = re.sub(r'\'{2,}', '', v)
        d[k] = s
    return d


def proc27():
    d = {}
    for k, v in proc26().iteritems():
        s = re.sub(r'\[\[(.+?)((#.+?)?\|(.+?))?\]\]', '\g<1>', v)
        d[k] = s
        print(k, s)
    return d


def main():
    if len(sys.argv) < 2:
        print('usage: python {} NUM'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    num = int(sys.argv[1])
    eval('proc{}()'.format(num))


if __name__ == '__main__':
    set_encoding()
    main()
