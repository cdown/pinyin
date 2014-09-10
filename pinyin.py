#!/usr/bin/env python
# vim: set fileencoding=utf8 :

from __future__ import unicode_literals
import re


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
