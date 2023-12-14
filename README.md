# FastAPI And Babel
![FastAPI And Babel](https://raw.githubusercontent.com/heysaeid/fastapi-and-babel/master/docs/img/logo/Color%20logo%20-%20no%20background.png)

[![Package version](https://img.shields.io/pypi/v/fastapi-and-babel?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi-and-babel/)
[![Downloads](https://img.shields.io/pypi/dm/fastapi-and-babel)](https://pypi.org/project/fastapi-and-babel/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi-and-babel.svg?color=%2334D058)](https://pypi.org/project/fastapi-and-babel/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/heysaeid/fastapi-and-babel/blob/master/LICENSE)

FastAPIAndBabel allows you to easily use babel in your FastAPI projects and offers some features to improve and ease things.


## Install 
You can either download the source code of this repository or install it via pip:
```
pip install fastapi-and-babel
```

## Usage
First, we create an instance of FastAPIAndBabel in our program as shown below
‍‍‍
```
from fastapi import FastAPI
from fastapi_and_babel.translator import FastAPIAndBabel


app = FastAPI()
translator = FastAPIAndBabel(__file__, app, "en")
```
We create the following mapping file
babel.cfg
```
[python: **.py]
```

Save the file and then run the following command
```
pybabel extract -F babel.cfg -o messages.pot .
```

babel uses this file for mapping and stores the patterns in messages.pot

```
pybabel init -i messages.pot -d translations -l en
```
Here -d says to save translations in translations, you can change it in config

After adding your messages, use the following command to compile

```pybabel compile -d translations```


Now we can translate our texts using the gettext method
```
from fastapi_and_babel import gettext as _

@app.get("/")
def index():
    return {"text": _("Hello World!")}
```