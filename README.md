# Reducing links with Bitly

This program shortens the entered link, or provides statistics on the shortened link.

### Installing

The API TOKEN must be taken from bitly.com after registration
You need to create a file .env and write there your key without quotes
```
TOKEN=Bearer 'your TOKEN'
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

If you want to reduce link, you need add only full url and programm will give you reduced link:
```
$ python main.py https://pikabu.ru/
bit.ly/2IWLf0P
```

If you want to get statistics on an reduced link you need add only reduced link and programm will give you daily statistics:
```
$ python main.py bit.ly/2IWLf0P
08.03.2019 - 1 clicks
06.03.2019 - 6 clicks
```
