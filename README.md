# Arabic to Roman numerals

> _This project converts any Arabic numerals to their equivalent Roman numerals using the [subtravtive method](https://en.wikipedia.org/wiki/Roman_numerals#Irregular_subtractive_notation)._


## Quick start

**1. Create a virtual env**

    python3 -m venv venv

then

    source venv/bin/activate

> _Alternatively, you can also use third-party tools like [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or [pipenv](https://pipenv.pypa.io/en/latest/) to better manage virtual environments._


**2. Install required packages**

    pip install -r requirements.txt


**3. Run tests**

    pytest -vvv


**4. Run the script**

    python3 arabic_to_roman.py <number>

> _The script accepts an Arabic numeral as an argument. Since this is the only argument, we accept it using `sys.argv`. For complex command-line arguments we can use thrid-party packages like [argparse](https://docs.python.org/3/library/argparse.html) or [click](https://click.palletsprojects.com/en/7.x/)._


## Structure

- The project has the following structure:
```
.
├── arabic_to_roman.py
├── README.md
├── requirements.txt
├── setup.cfg
└── test_arabic_to_roman.py
```

- Function signature
```
"""Convert arabic numeral to roman numeral.

Args:
    num (int): Arabic numeral.

Returns:
    str: Roman equivalent of `num` passed.

Raises:
    InvalidNumeralException: This exception is raised when the `num` passed is either
        non-integer or an integer less than or equal to zero.

Example:
    >>> print(convert_to_roman(9))
    IX
"""
```

