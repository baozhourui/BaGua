# BaGua
> 科学占卜, 计算机算命.

[![PyPI Downloads][pypi-dl-image]][pypi-dl-link]
[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Build Status][travis-image]][travis-link]

### Environment
- Python  
    2.7

### Install  
- pip  
`pip install bagua`  

- location
```shell
git clone https://github.com/FloydaGithub/BaGua.git
cd BaGua
python setup.py install
```

### Usage  
- Termianl  
```shell
$ bagua
Usage:
  bagua <index>
  bagua -r
  bagua -s <keyword>
  bagua -v

$ bagua 1
-----           上九: 亢龍有悔.
-----           九五: 飛龍在天, 利見大人.
-----           九四: 或躍在淵, 無咎.
-----           九三: 君子終日乾乾, 夕惕若, 厲, 無咎.
-----           九二: 見龍再田, 利見大人.
-----           初九: 潛龍勿用.
http://baike.fututa.com/a5738/
```

- Python Library  
```
import bagua
bagua.show(1)
```

[pypi-dl-image]: https://img.shields.io/pypi/dm/BaGua.png
[pypi-dl-link]: https://pypi.python.org/pypi/BaGua
[pypi-v-image]: https://img.shields.io/pypi/v/BaGua.png
[pypi-v-link]: https://pypi.python.org/pypi/BaGua
[travis-image]: https://img.shields.io/travis/FloydaGithub/BaGua/master.png
[travis-link]: https://travis-ci.org/FloydaGithub/BaGua