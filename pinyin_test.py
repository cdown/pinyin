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


def test_word_num_to_inline():
    eq('nǚ', pinyin.num_to_inline('nü3'))


def test_multi_word_num_to_inline():
    eq('nǚ rén', pinyin.num_to_inline('nü3 ren2'))


def test_multi_word_num_to_inline_toneless():
    eq('zhuō zi', pinyin.num_to_inline('zhuo1 zi'))


def test_multi_word_numbers():
    eq('wǒ yǒu 25 kuài yuán', pinyin.num_to_inline('wo3 you3 25 kuai4 yuan2'))
