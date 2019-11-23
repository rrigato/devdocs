# Development Standards
This documentation provides an overview of development best practices across python, sql, continuous integration

## Table of contents

- [Python](#python)
    * [Python Documentation](#pythondocumentation)
    * [Python Tests](#pythontests)

- [SQL](#sql)
    * [SQL Table Creation](#sqltablecreation)
    * [SQL Subqueries](#sqlsubqueries)

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

Write unit, integration and end-to-end tests using the built in [unittest module](https://docs.python.org/3/library/unittest.html)

Code coverage should be built into html files using the coverage [module] (https://coverage.readthedocs.io/en/v4.5.x/)


# SQL

## SQL Table Creation
Always use subqueries instead of creating temporary tables. The only table created should be the final output table

Always have a primary key on the table.

## SQL Subqueries

Always provide a meaningful alias for the subquery. Ex:

```
(
    --Querying weather data
) WEATHER_DATA
```


Above each subquery provide a block comment which provides an overview of the subquery and the unique columns from the subquery. Ex:

```
-------------------------
--My block comment explaining domain knowledge from
--FOO_FIELDS subquery
--
--PK is COL1 and COL2
--SELECT COUNT(*), COUNT(DISTINCT COL1 || COL2)

--100, 100
-------------------------
(
    SELECT COL1, COL2, etc..
    FROM FOO
)FOO_FIELDS
```