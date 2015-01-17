[![Linux build status][travis-image]][travis-builds]
[![Windows build status][appveyor-image]][appveyor-builds]
[![Coverage][coveralls-image]][coveralls]
[![Code health][landscape-image]][landscape]
[![Dependencies][requires-image]][requires]

[travis-builds]: https://travis-ci.org/cdown/pinyin
[travis-image]: https://img.shields.io/travis/cdown/pinyin/master.svg?label=linux
[appveyor-builds]: https://ci.appveyor.com/project/cdown/pinyin
[appveyor-image]: https://img.shields.io/appveyor/ci/cdown/pinyin/master.svg?label=windows
[coveralls]: https://coveralls.io/r/cdown/pinyin
[coveralls-image]: https://img.shields.io/coveralls/cdown/pinyin/master.svg
[landscape]: https://landscape.io/github/cdown/pinyin/master
[landscape-image]: https://landscape.io/github/cdown/pinyin/master/landscape.svg
[requires]: https://requires.io/github/cdown/pinyin/requirements/?branch=master
[requires-image]: https://img.shields.io/requires/github/cdown/pinyin.svg?label=deps

pinyin is a small library to manipulate [Hanyu Pinyin][].

[Hanyu Pinyin]: http://en.wikipedia.org/wiki/Pinyin

## Usage

Right now there is quite limited functionality, but you can do stuff like this:

```python
>>> pinyin.num_to_inline('wo3 you3 25 kuai4')
'wǒ yǒu 25 kuài'
```

## Installation

pinyin isn't on PyPi yet. For now, you can download it and run it by itself (it
has no external dependencies).

## Testing

    $ pip install -r tests/requirements.txt
    $ nosetests

## License

pinyin is licensed under an
[ISC license](http://en.wikipedia.org/wiki/ISC_license). Full information is in
[LICENSE.md](LICENSE.md).
