#!/usr/bin/env python
# vim: set fileencoding=utf8 :

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

    max_idx = None

    for vowel in ['a', 'e', 'i', 'o', 'u', 'v', 'ü']:
        last_vowel = word.rfind(vowel)
        if last_vowel != -1 and last_vowel > max_idx:
            max_idx = last_vowel

    if max_idx is not None:
        return word[max_idx]
    else:
        return None


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


def num_to_inline(pinyin):
    '''
    Returns the input string, with numbered tones replaced with Unicode.

    :param pinyin_original: pinyin text that includes numbered tones
    :returns: the input string, using Unicode replacements for numbered tones
    '''

    word_tones = []
    output = []

    words = pinyin.split()

    for word in words:
        try:
            tone = int(word[-1])
        except ValueError:
            tone = None

        word = word[:-1]
        word_tones.append((word, tone))

    for word, tone in word_tones:
        char_to_change = tone_vowel(word)
        char_tone_unicode = tonify_char(char_to_change, tone)
        unicode_tone_word = word.replace(char_to_change, char_tone_unicode)
        output.append(unicode_tone_word)

    return ' '.join(output)
