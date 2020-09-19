# Python Stateless Defaults
A Python decorator to make default arguments in functions stateless.

```python
from stateless_defaults import stateless_defaults

@stateless_defaults()
def append_to_list(a, l=[]):
    l.append(a)
    return l
```

## What is this thing??
In Python there a well-known surprising behavior regarding default arguments for functions.
Take a look at this function for example:
```python
def append_to_list(a, l=[]):
    l.append(a)
    return l
```
Seems legit. Lets call it:
```python
>>> append_to_list(10)
[10]
```
Very nice. We get a list with the number 10 in it.
But watch what happen when we try to call it again:
```python
>>> append_to_list(20)
[10, 20]
```
Ho No! Somehow the function remembered the result returned in the previous call, and appended the new value to it! 
What went wrong!?

This happens because the default arguments of the function are evaluated once at function definition,
and they remain until the function is out-of-scope and garbage-collected. So when we put a `list` as a default argument,
it stays there! The same list is referenced every time we call the function without the `l` parameter.

The little piece of code in the repository is a function decorator that eliminates this behavior by 
providing new defaults every time your function is called.

**Note:** This only works by default on the mutable types `list`, `dict`, `set` and `deque` 
(and any subclass of them like `OrderedDict`). You may override those types like so:
```python
@stateless_defaults(supported_types=(dict,))
def my_function...
``` 
