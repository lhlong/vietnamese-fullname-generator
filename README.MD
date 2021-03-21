# VIETNAMESE FULLNAME GENERRATOR

This tool will help to generate a common fullname in Vietnamese.

## Data Source

- Get data male/female name from [Vietnamese Name Dict](https://github.com/duyet/vietnamese-namedb)
- Get common firstname [Wiki](https://vi.wikipedia.org/wiki/H%E1%BB%8D_ng%C6%B0%E1%BB%9Di_Vi%E1%BB%87t_Nam)

## How to run

>pip install vn_fullname_generator

```python
from vn_fullname_generator import generator
gender = 1
generator.generate(gender)
'Trần Văn Minh'
```
