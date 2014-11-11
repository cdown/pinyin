#!/usr/bin/env python
# vim: set fileencoding=utf8 :

"""
Generic library for manipulating Hanyu Pinyin.
"""

from __future__ import unicode_literals
import re


TONE_REPLACEMENTS = {
    'a': ['ā', 'á', 'ǎ', 'à'],
    'e': ['ē', 'é', 'ě', 'è'],
    'i': ['ī', 'í', 'ǐ', 'ì'],
    'o': ['ō', 'ó', 'ǒ', 'ò'],
    'u': ['ū', 'ú', 'ǔ', 'ù'],
    'v': ['ǖ', 'ǘ', 'ǚ', 'ǜ'],
    'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ'],
}


def tone_vowel(word):
    '''
    Find which character to put the tone over, using standard Pinyin rules.

    The rules are:

    - If there is an a or an e, the tone goes on the a or the e. No pinyin
      syllable contains both an a and an e.
    - In the ou combination, the o takes the tone mark.
    - In all other cases, the final vowel gets the tone mark.

    :param word: a word to find the character to put the tone mark over
    :returns: the character to put the tone over
    '''

    vowel_types = {
        'a': 'a',
        'e': 'e',
        'ou': 'o',
    }

    for vowel_type in vowel_types:
        if vowel_type in word:
            return vowel_types[vowel_type]

    last_vowel = re.search('.*([aeiouvü])', word)
    if last_vowel is None:
        return None

    return last_vowel.group(1)


def tonify_char(char, tone):
    '''
    Given a character and a tone, determine what Unicode should be used to
    represent it.

    :param char: a character without a tone
    :param tone: the tone number to use
    :returns: a unicode char representing this char/tone combination
    '''

    if tone is None:
        return char
    return TONE_REPLACEMENTS[char][tone - 1]


def split_word_and_tone(word):
    '''
    Split a word from its tone.

    :param word: a word, potentially with a tone
    :returns: a tuple of (word, tone)
    '''

    if word.isdigit():
        # This is likely raw Arabic numerals.
        return word, None
    else:
        try:
            tone = int(word[-1])
        except ValueError:
            return word, None
        else:
            return word[:-1], tone


def numbered_word_to_diacritic(pinyin):
    '''
    Converts a word with a numbered tone ("you2") to a word with a diacritic
    tone ("yóu").

    :param pinyin: a pinyin word with a numbered tone
    :returns: the same pinyin word with a diacritic tone
    '''

    word, tone = split_word_and_tone(pinyin)
    char_to_change = tone_vowel(word)

    if char_to_change is None:
        return word

    char_tone_unicode = tonify_char(char_to_change, tone)
    unicode_tone_word = word.replace(char_to_change, char_tone_unicode)

    return unicode_tone_word


def num_to_inline(pinyin):
    '''
    Returns the input string, with numbered tones replaced with Unicode.

    :param pinyin_original: pinyin text that includes numbered tones
    :returns: the input string, using Unicode replacements for numbered tones
    '''

    words = pinyin.split()
    return ' '.join(numbered_word_to_diacritic(word) for word in words)
