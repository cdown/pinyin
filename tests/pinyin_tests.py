#!/usr/bin/env python
# vim: set fileencoding=utf8 :

"""
Test suite for pinyin, a library to manipulate Hanyu Pinyin.
"""

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


def test_numbered_word_to_diacritic():
    eq('nǚ', pinyin.numbered_word_to_diacritic('nü3'))


def test_numbered_word_to_diacritic_none():
    eq('nü', pinyin.numbered_word_to_diacritic('nü'))


def test_word_num_to_inline():
    eq('nǚ', pinyin.num_to_inline('nü3'))


def test_multi_word_num_to_inline():
    eq('nǚ rén', pinyin.num_to_inline('nü3 ren2'))


def test_multi_word_num_to_inline_toneless():
    eq('zhuō zi', pinyin.num_to_inline('zhuo1 zi'))


def test_multi_word_numbers():
    eq('wǒ yǒu 25 kuài', pinyin.num_to_inline('wo3 you3 25 kuai4'))


def test_split_word_and_tone():
    eq(('ai', 4), pinyin.split_word_and_tone('ai4'))


def test_split_word_and_tone_none():
    eq(('zi', None), pinyin.split_word_and_tone('zi'))


def test_split_word_and_tone_arabic_number():
    eq(('2048', None), pinyin.split_word_and_tone('2048'))
