Populace
========

Usage
-----

Install dependencies

```
$ pip install -r requirements.txt
```

Then use in your python scripts as follows:

```python
from populace import find_users

users = find_users("London")
```

### `find_users(city, radius=50)`

This function will get a combined list of users living in the provided city, or
within a given radius of the city's geographical center. Merges results of
`living_in` and `currently_near` and removes duplicates.


### `living_in(city)`

This function will get a list of users living in a given city


### `currently_near(city, radius=50)`

This function will get a list of users within a given radius of the provided
city's geographical center.


Testing
-------

You'll need to install `nose2` to run the tests. If you've already done a `pip
install` then you should already have it.
Then run

```
$ python - m nose2
```

And check the output
