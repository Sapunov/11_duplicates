# 11_duplicates

Утилита для поиска файлов-дупликатов в директории.

```{r, engine='bash'}
$ python duplicates.py --help
usage: duplicates.py [-h] -d DIRECTORY

Find duplicate files in DIRECTORY

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Directory to find duplicates
```

**Что считается дупликатом:** файлы, которые имеют одинаковые имена и размеры

> 11 задача с сайта [devman.org](https://devman.org/) - решай задачи и читай учебный материал


## Использование

```{r, engine='bash'}
$ python duplicates.py -d ~/Documents/
Duplicates founded: 2
---------------------
* /home/nsapunov/Documents/СКОРОЧТЕНИЕ.png
* /home/nsapunov/Documents/BEC Vantage Testbuilder/СКОРОЧТЕНИЕ.png
---------------------
* /home/nsapunov/Documents/1 занятие. тестировани.odt
* /home/nsapunov/Documents/xmind/1 занятие. тестировани.odt
```

> Скрипт использует python 3 версии.


## Лицензия

[Creative Commons Attribution License](http://creativecommons.org/licenses/by/2.0/)
