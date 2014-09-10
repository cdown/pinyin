#!/usr/bin/env python
# vim: set fileencoding=utf8 :

from __future__ import unicode_literals
from nose.tools import eq_ as eq
import pinyin


def test_tone_vowel():
    expected = (
        ('shuang3', 'a'),
        ('mang3', 'a'),
        ('meng3', 'e'),
        ('ming3', 'i'),
        ('mou3', 'o'),
        ('nü3', 'ü'),
        ('nv3', 'v'),
    )

    for word, expected_vowel in expected:
        eq(expected_vowel, pinyin.tone_vowel(word))


def test_tonify_char():
    eq('ǘ', pinyin.tonify_char('ü', 2))


def test_tonify_char_none():
    eq('ü', pinyin.tonify_char('ü', None))
