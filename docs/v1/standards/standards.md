# Development Standards
This documentation provides an overview of development best practices across python, sql, continuous integration

## Table of contents

- [Python](#python)
    * [Python Documentation](#python-documentation)
    * [Python Tests](#python-tests)

- [Paragraphs](#paragraphs)
- [Headings](#headings)
    * [Atx Style](#atx-style)
    * [Setext style](#setext-style)
    * [Header IDs](#header-ids)

## Python

### Python Documentation
Follow the [numpy docstring format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) for each function/class. Ex:

```
def new_function(arg_one):
    '''One sentance that describes what the function does

        Parameters
        ----------
        arg_one : str
            the first arguement passed to the function

        Returns
        -------
        success_ind : int
            0 if success, 1 if failure

        Raises
        ------
        AE : AssertionError
            Raises an assertion error if best practices are not being followed
    '''
```

Build python documentation into html files using sphinx [sphinx](http://www.sphinx-doc.org/en/master/)


## Python Tests

Code Coverage should be 80% or higher.

Write unit, integration and end-to-end tests using the built in [unittest module]()
